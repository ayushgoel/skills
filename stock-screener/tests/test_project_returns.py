import importlib.util
import math
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "project_returns.py"
SPEC = importlib.util.spec_from_file_location("project_returns", SCRIPT_PATH)
assert SPEC and SPEC.loader
PROJECT_RETURNS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PROJECT_RETURNS)


class ProjectReturnsTest(unittest.TestCase):
    def test_flat_multiple_matches_eps_growth_without_dividends(self):
        result = PROJECT_RETURNS.project_returns(
            {
                "current_price": 200,
                "current_eps": 10,
                "horizon_years": 5,
                "scenarios": [
                    {"name": "Base", "eps_cagr_pct": 10, "exit_multiple": 20}
                ],
            }
        )

        scenario = result["scenarios"][0]
        self.assertAlmostEqual(scenario["price_cagr_pct"], 10)
        self.assertAlmostEqual(scenario["terminal_wealth_cagr_pct"], 10)
        self.assertAlmostEqual(scenario["cash_flow_irr_pct"], 10)
        self.assertAlmostEqual(scenario["multiple_cagr_pct"], 0)

    def test_multiple_compression_offsets_eps_growth(self):
        result = PROJECT_RETURNS.project_returns(
            {
                "current_price": 400,
                "current_eps": 10,
                "horizon_years": 5,
                "scenarios": [
                    {"name": "Compression", "eps_cagr_pct": 10, "exit_multiple": 20}
                ],
            }
        )

        scenario = result["scenarios"][0]
        expected_price_cagr = 1.1 * math.pow(0.5, 1 / 5) - 1
        self.assertAlmostEqual(scenario["price_cagr_pct"], expected_price_cagr * 100)
        self.assertLess(scenario["price_cagr_pct"], 0)

    def test_dividends_increase_total_shareholder_return(self):
        result = PROJECT_RETURNS.project_returns(
            {
                "current_price": 100,
                "current_eps": 10,
                "horizon_years": 3,
                "scenarios": [
                    {
                        "name": "Income",
                        "eps_cagr_pct": 0,
                        "exit_multiple": 10,
                        "next_annual_dividend": 4,
                        "dividend_cagr_pct": 0,
                    }
                ],
            }
        )

        scenario = result["scenarios"][0]
        self.assertEqual(scenario["cumulative_dividends"], 12)
        self.assertGreater(scenario["terminal_wealth_cagr_pct"], scenario["price_cagr_pct"])
        self.assertAlmostEqual(scenario["cash_flow_irr_pct"], 4)
        self.assertGreater(scenario["cash_flow_irr_pct"], scenario["terminal_wealth_cagr_pct"])

    def test_calculates_entry_price_supported_by_hurdle(self):
        result = PROJECT_RETURNS.project_returns(
            {
                "current_price": 100,
                "current_eps": 10,
                "horizon_years": 2,
                "hurdle_rate_pct": 10,
                "scenarios": [
                    {"name": "Base", "eps_cagr_pct": 10, "exit_multiple": 10}
                ],
            }
        )

        scenario = result["scenarios"][0]
        self.assertAlmostEqual(scenario["max_entry_price_at_hurdle"], 100)
        self.assertAlmostEqual(scenario["entry_price_gap_pct"], 0)
        self.assertIn("Max entry at IRR hurdle", PROJECT_RETURNS.render_markdown(result))

    def test_entry_price_discounts_dividends_when_paid(self):
        payload = {
            "current_price": 100,
            "current_eps": 10,
            "horizon_years": 3,
            "hurdle_rate_pct": 10,
            "scenarios": [
                {
                    "name": "Income",
                    "eps_cagr_pct": 0,
                    "exit_multiple": 10,
                    "next_annual_dividend": 4,
                }
            ],
        }
        scenario = PROJECT_RETURNS.project_returns(payload)["scenarios"][0]
        expected_entry = 4 / 1.1 + 4 / 1.1**2 + 104 / 1.1**3
        self.assertAlmostEqual(scenario["max_entry_price_at_hurdle"], expected_entry)

        payload["current_price"] = expected_entry
        repriced = PROJECT_RETURNS.project_returns(payload)["scenarios"][0]
        self.assertAlmostEqual(repriced["cash_flow_irr_pct"], 10)

    def test_negative_return_is_solved(self):
        scenario = PROJECT_RETURNS.project_returns(
            {
                "current_price": 200,
                "current_eps": 10,
                "horizon_years": 2,
                "scenarios": [
                    {"name": "Loss", "eps_cagr_pct": 0, "exit_multiple": 5}
                ],
            }
        )["scenarios"][0]
        self.assertAlmostEqual(scenario["cash_flow_irr_pct"], -50)

    def test_large_return_expands_irr_search(self):
        scenario = PROJECT_RETURNS.project_returns(
            {
                "current_price": 10,
                "current_eps": 10,
                "horizon_years": 1,
                "scenarios": [
                    {"name": "Upside", "eps_cagr_pct": 0, "exit_multiple": 10}
                ],
            }
        )["scenarios"][0]
        self.assertAlmostEqual(scenario["cash_flow_irr_pct"], 900)

    def test_rejects_non_positive_eps(self):
        with self.assertRaisesRegex(ValueError, "current_eps must be greater than zero"):
            PROJECT_RETURNS.project_returns(
                {
                    "current_price": 100,
                    "current_eps": 0,
                    "horizon_years": 5,
                    "scenarios": [
                        {"name": "Base", "eps_cagr_pct": 10, "exit_multiple": 20}
                    ],
                }
            )


if __name__ == "__main__":
    unittest.main()
