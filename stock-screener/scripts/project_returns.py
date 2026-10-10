#!/usr/bin/env python3
"""Project P/E returns with dividend timing and an IRR-consistent entry hurdle."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


def _finite_number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{field} must be finite")
    return number


def _positive_number(value: Any, field: str) -> float:
    number = _finite_number(value, field)
    if number <= 0:
        raise ValueError(f"{field} must be greater than zero")
    return number


def _percentage(value: Any, field: str) -> float:
    percentage = _finite_number(value, field)
    if percentage <= -100:
        raise ValueError(f"{field} must be greater than -100")
    return percentage / 100


def _present_value(cash_flows: list[float], rate: float) -> float:
    return sum(cash / (1 + rate) ** year for year, cash in enumerate(cash_flows, 1))


def _cash_flow_irr(current_price: float, cash_flows: list[float]) -> float:
    # Nonnegative future proceeds give one IRR for an initial purchase outflow.
    lower, upper = -1.0, 1.0
    while _present_value(cash_flows, upper) > current_price:
        upper = 2 * upper + 1
    for _ in range(100):
        midpoint = (lower + upper) / 2
        if _present_value(cash_flows, midpoint) > current_price:
            lower = midpoint
        else:
            upper = midpoint
    return (lower + upper) / 2


def project_scenario(
    *,
    current_price: float,
    current_eps: float,
    horizon_years: int,
    hurdle_rate: float | None,
    scenario: dict[str, Any],
) -> dict[str, Any]:
    name = str(scenario.get("name", "Unnamed"))
    eps_cagr = _percentage(scenario.get("eps_cagr_pct"), f"{name}.eps_cagr_pct")
    exit_multiple = _positive_number(
        scenario.get("exit_multiple"), f"{name}.exit_multiple"
    )
    next_dividend = _finite_number(
        scenario.get("next_annual_dividend", 0), f"{name}.next_annual_dividend"
    )
    if next_dividend < 0:
        raise ValueError(f"{name}.next_annual_dividend cannot be negative")
    dividend_cagr = _percentage(
        scenario.get("dividend_cagr_pct", 0), f"{name}.dividend_cagr_pct"
    )

    entry_multiple = current_price / current_eps
    terminal_eps = current_eps * (1 + eps_cagr) ** horizon_years
    terminal_price = terminal_eps * exit_multiple
    dividends = [
        next_dividend * (1 + dividend_cagr) ** year
        for year in range(horizon_years)
    ]
    cumulative_dividends = sum(dividends)
    cash_flows = dividends.copy()
    cash_flows[-1] += terminal_price
    terminal_wealth = terminal_price + cumulative_dividends
    price_cagr = (terminal_price / current_price) ** (1 / horizon_years) - 1
    terminal_wealth_cagr = (terminal_wealth / current_price) ** (1 / horizon_years) - 1
    cash_flow_irr = _cash_flow_irr(current_price, cash_flows)
    multiple_cagr = (exit_multiple / entry_multiple) ** (1 / horizon_years) - 1

    result = {
        "name": name,
        "eps_cagr_pct": eps_cagr * 100,
        "exit_multiple": exit_multiple,
        "multiple_cagr_pct": multiple_cagr * 100,
        "terminal_eps": terminal_eps,
        "terminal_price": terminal_price,
        "price_cagr_pct": price_cagr * 100,
        "cumulative_dividends": cumulative_dividends,
        "terminal_wealth_cagr_pct": terminal_wealth_cagr * 100,
        "cash_flow_irr_pct": cash_flow_irr * 100,
    }
    if hurdle_rate is not None:
        max_entry_price = _present_value(cash_flows, hurdle_rate)
        result["max_entry_price_at_hurdle"] = max_entry_price
        result["entry_price_gap_pct"] = (max_entry_price / current_price - 1) * 100
    return result


def project_returns(payload: dict[str, Any]) -> dict[str, Any]:
    current_price = _positive_number(payload.get("current_price"), "current_price")
    current_eps = _positive_number(payload.get("current_eps"), "current_eps")
    horizon = payload.get("horizon_years")
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon <= 0:
        raise ValueError("horizon_years must be a positive integer")
    hurdle_rate = None
    if "hurdle_rate_pct" in payload:
        hurdle_rate = _percentage(payload["hurdle_rate_pct"], "hurdle_rate_pct")
    scenarios = payload.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        raise ValueError("scenarios must be a non-empty list")
    if not all(isinstance(scenario, dict) for scenario in scenarios):
        raise ValueError("each scenario must be an object")

    result = {
        "current_price": current_price,
        "current_eps": current_eps,
        "entry_multiple": current_price / current_eps,
        "horizon_years": horizon,
        "scenarios": [
            project_scenario(
                current_price=current_price,
                current_eps=current_eps,
                horizon_years=horizon,
                hurdle_rate=hurdle_rate,
                scenario=scenario,
            )
            for scenario in scenarios
        ],
    }
    if hurdle_rate is not None:
        result["hurdle_rate_pct"] = hurdle_rate * 100
    return result


def render_markdown(result: dict[str, Any]) -> str:
    hurdle_rate = result.get("hurdle_rate_pct")
    lines = [
        f"Entry P/E: {result['entry_multiple']:.2f}x",
        f"Horizon: {result['horizon_years']} years",
        "Dividends: annual year-end payments; terminal wealth holds them as idle cash.",
    ]
    if hurdle_rate is not None:
        lines.append(f"Return hurdle: {hurdle_rate:.2f}%")
    lines.extend(
        [
            "",
            "| Scenario | EPS CAGR | Exit P/E | Multiple CAGR | Terminal EPS | "
            "Terminal price | Price CAGR | Cumulative dividends | "
            "Terminal-wealth CAGR | Cash-flow IRR |"
            + (" Max entry at IRR hurdle |" if hurdle_rate is not None else ""),
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"
            + (" ---: |" if hurdle_rate is not None else ""),
        ]
    )
    for scenario in result["scenarios"]:
        row = (
            "| {name} | {eps_cagr_pct:.2f}% | {exit_multiple:.2f}x | "
            "{multiple_cagr_pct:.2f}% | {terminal_eps:.2f} | {terminal_price:.2f} | "
            "{price_cagr_pct:.2f}% | {cumulative_dividends:.2f} | "
            "{terminal_wealth_cagr_pct:.2f}% | {cash_flow_irr_pct:.2f}% |".format(**scenario)
        )
        if hurdle_rate is not None:
            row += " {max_entry_price_at_hurdle:.2f} |".format(**scenario)
        lines.append(row)
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Project P/E-based returns from a JSON scenario file."
    )
    parser.add_argument("input", type=Path, help="Path to the JSON input")
    parser.add_argument(
        "--format", choices=("markdown", "json"), default="markdown"
    )
    parser.add_argument("--output", type=Path, help="Optional output path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("input JSON must be an object")
        result = project_returns(payload)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        raise SystemExit(f"error: {error}") from error

    output = (
        json.dumps(result, indent=2) + "\n"
        if args.format == "json"
        else render_markdown(result)
    )
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
