#!/usr/bin/env python3
"""Project P/E-based price and shareholder returns across scenarios."""

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
    cumulative_dividends = sum(
        next_dividend * (1 + dividend_cagr) ** year
        for year in range(horizon_years)
    )
    terminal_wealth = terminal_price + cumulative_dividends
    price_cagr = (terminal_price / current_price) ** (1 / horizon_years) - 1
    annualized_tsr = (terminal_wealth / current_price) ** (1 / horizon_years) - 1
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
        "annualized_tsr_pct": annualized_tsr * 100,
    }
    if hurdle_rate is not None:
        max_entry_price = terminal_wealth / (1 + hurdle_rate) ** horizon_years
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
    ]
    if hurdle_rate is not None:
        lines.append(f"Return hurdle: {hurdle_rate:.2f}%")
    lines.extend(
        [
            "",
            "| Scenario | EPS CAGR | Exit P/E | Multiple CAGR | Terminal EPS | "
            "Terminal price | Price CAGR | Cumulative dividends | Annualized TSR |"
            + (" Max entry at hurdle |" if hurdle_rate is not None else ""),
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"
            + (" ---: |" if hurdle_rate is not None else ""),
        ]
    )
    for scenario in result["scenarios"]:
        row = (
            "| {name} | {eps_cagr_pct:.2f}% | {exit_multiple:.2f}x | "
            "{multiple_cagr_pct:.2f}% | {terminal_eps:.2f} | {terminal_price:.2f} | "
            "{price_cagr_pct:.2f}% | {cumulative_dividends:.2f} | "
            "{annualized_tsr_pct:.2f}% |".format(**scenario)
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
