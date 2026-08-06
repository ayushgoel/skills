---
name: portfolio-analysis
description: Analyze listed stocks or an equity portfolio, including CSV holdings, and discover or monitor index-aware mid-cap and catalyst-growth opportunities using current primary-source evidence, normalized per-share fundamentals, valuation, promoter transactions, scenario-based return decomposition, and portfolio risk. Use to review stocks, compare holdings, find opportunities beyond an existing index core, maintain entry/scale/trim/exit watchlists, or produce evidence-based portfolio decisions rather than react to recent ticker returns.
---

# Portfolio Analysis

Analyze prospective returns through business performance, valuation, cash returns,
and portfolio fit. Do not infer quality from recent price movement or make a decision
from a single ratio.

## Workflow

1. Establish the as-of date, market, horizon, currency, return hurdle, risk needs,
   liquidity needs, tax constraints, desired actions, and portfolio boundary. Include
   index funds and externally held equity when the user discloses them. If context is
   missing, state reasonable illustrative assumptions instead of inventing facts.
   Do not recommend direct mega-cap exposure as diversification when the user's index
   funds already provide it.
2. For a portfolio CSV, extract the security identifier, quantity, and acquisition
   price. Remove zero-quantity rows and combine duplicates using quantity-weighted
   acquisition cost. Write `<input-stem>.cleaned.csv` beside the input unless that
   directory is this public skill repository; in that case, use a private temporary
   workspace or a user-approved output directory.
3. Read [references/two-engine-framework.md](references/two-engine-framework.md)
   completely before researching or rating a company. For mid-cap discovery or when
   the user already has an index core, also read
   [references/mid-cap-opportunity-framework.md](references/mid-cap-opportunity-framework.md)
   completely. For volatile growth, turnaround, order-book, capacity-expansion, or
   catalyst-led companies, also read
   [references/catalyst-watchlist-framework.md](references/catalyst-watchlist-framework.md)
   completely.
4. Gather current, dated evidence. Prefer exchange filings, regulatory filings,
   company results and presentations, conference-call transcripts, and official
   transaction disclosures. Use secondary sources for context, not as substitutes
   for material primary facts. Cite sources and distinguish facts, estimates, and
   inferences.
5. Normalize the economic record. Reconcile reported and diluted per-share figures;
   remove material one-offs; inspect share-count changes, cyclicality, leverage,
   capitalized costs, acquisitions, and cash conversion. Never annualize one quarter
   without explaining seasonality.
6. Select the appropriate valuation lens. Use P/E only when positive normalized EPS
   represents the business. Use the sector-specific alternatives in the reference
   when P/E is misleading.
7. Assess the EPS engine, valuation engine, promoter signal, dividends and buybacks,
   balance-sheet risk, and thesis invalidators. Do not count buybacks twice: their
   share-count effect belongs in EPS; cash dividends belong in total return.
8. Build bear, base, and bull scenarios over the stated horizon. When P/E is valid,
   run `scripts/project_returns.py` using a temporary JSON input outside this source
   repository. Report EPS growth, multiple change, dividend contribution, price
   CAGR, and annualized total shareholder return separately. Compare each case with
   the return hurdle and calculate the maximum entry price supported by that case.
9. Assign `Discover`, `Validate`, `Starter`, `Scale/Add`, `Hold`, `Trim`, or
   `Exit/Archive`. Base the state on prospective return, downside, thesis quality,
   evidence maturity, confidence, concentration, taxes, and opportunity cost—not
   acquisition price or past return alone. Map `Discover` and `Validate` to `Watch`
   in compact action summaries. Do not use `Exit` solely because valuation is rich
   while the operating thesis remains intact; normally use `Hold/Watch` or `Trim`.
10. For a portfolio, aggregate position weights, sector and factor concentration,
    balance-sheet and governance risks, liquidity, correlated thesis failures, and
    the effect of proposed trades. Do not impose a fixed HNI or 80/20 allocation.
11. When opportunity discovery is in scope, build a current mid-cap candidate funnel
    beyond existing holdings. Use the current regulator/AMFI or exchange classification
    rather than a stale fixed market-cap threshold. Compare candidates with relevant
    mid-cap peers and retain only ideas that pass the reference's quality, governance,
    liquidity, valuation, and evidence gates. A watchlist is preferable to a forced buy.

## Portfolio Mandate and Opportunity Discovery

- Treat disclosed index funds as the core exposure. Analyze held large caps and flag
  exceptional opportunities, but do not let familiar index constituents crowd out
  mid-cap research or duplicate the core without a clear prospective-return advantage.
- Separate `core/index exposure`, `active compounders`, `cyclical opportunities`, and
  `catalyst-growth/emerging compounders`, and `speculative/research positions`.
  Evaluate concentration across the combined exposure.
- For new-money recommendations, prioritize the best risk-adjusted expected returns,
  with deliberate coverage of mid caps. Do not prefer a mid cap merely because of its
  size; require a longer runway, credible per-share earnings compounding, acceptable
  downside, and sufficient liquidity.
- Demand a higher margin of safety or return buffer for mid caps because estimates,
  liquidity, key-person dependence, customer concentration, and governance risk are
  usually wider than for large caps.
- Identify why an opportunity may be mispriced and what evidence can close that gap.
  Reject ideas whose base return requires speculative P/E expansion, peak margins, an
  unfinanced capacity plan, or unsupported market-share assumptions.
- Prefer a small, ranked shortlist of deeply researched candidates over a long screen.
  Give explicit buy zones, staged position-size ranges, monitoring events, and thesis
  invalidators; do not fill an allocation quota when no candidate clears the hurdle.

## Decision Discipline

- Use the user's hurdle rate. If absent, disclose an illustrative hurdle and show how
  the action changes at nearby hurdles.
- Treat an attractive base case as insufficient when the bear case risks permanent
  capital loss or depends on fragile financing or governance.
- Treat high-quality growth at a hostile valuation as a valuation problem, not
  automatically a business-quality problem.
- Distinguish volatility from permanent-capital-loss risk. A volatile company with a
  measurable, funded growth path may merit a capped starter position and catalyst
  watch even before it qualifies as a proven compounder.
- Reserve `Exit` for a broken thesis, unacceptable governance or financing risk, or a
  clearly superior use of capital after tax and position-size effects. Use `Trim` when
  price has outrun plausible earnings but the thesis remains valid.
- Treat a low multiple with weak normalized earnings as a possible value trap.
- Treat promoter buying as corroborating evidence, never as a substitute for
  operating evidence or valuation.
- Do not equate higher return potential with a smaller market cap. Require prospective
  per-share return to come primarily from earnings/book-value growth and cash returns,
  with a neutral or conservative valuation engine in the base case.
- State confidence as high, medium, or low and list the evidence that would change
  the action.

## Output

Write portfolio analysis beside the input as `<input-stem>.analysis.md`, except when
the input is inside this public skill repository. Keep runtime reports, downloads,
and intermediate data in the input directory, a private workspace, or a temporary
directory—never in this skill repository.

Include:

1. As-of date, horizon, assumptions, data gaps, and source policy.
2. Portfolio summary with concentration risks and prioritized actions.
   Show disclosed index exposure separately and explain where direct holdings overlap.
3. For each company:
   - position and acquisition details, with cost basis separated from forward value;
   - normalized operating record and accounting-quality notes;
   - EPS-engine rating and supporting evidence;
   - valuation-engine rating and appropriate valuation method;
   - bear/base/bull return table;
   - promoter transaction and pledge assessment;
   - dividends, buybacks, dilution, and capital allocation;
   - thesis, catalysts, risks, and explicit invalidators;
   - action, confidence, position-size implication, and concise rationale;
   - dated source links.
4. When opportunity discovery is requested, a ranked mid-cap shortlist containing:
   - current market-cap classification and liquidity evidence;
   - the differentiated thesis and source of potential mispricing;
   - EPS-engine, valuation-engine, governance, balance-sheet, and cash-conversion gates;
   - bear/base/bull returns, buy zone, initial and maximum position-size range;
   - catalyst path, invalidators, confidence, and dated primary sources;
   - screened candidates rejected and the decisive reason, to expose selection bias.
5. A final action queue: add, hold, trim, exit, and watch/research. Distinguish changes
   to existing holdings from new mid-cap ideas.
6. For catalyst-growth names, a watchlist dashboard containing the current state,
   thesis, dated baseline, next catalyst, operating KPIs, valuation/add zone, scale
   conditions, trim conditions, hard invalidators, position cap, review date, and
   source links. State which alerts require one quarter and which require confirmation
   across two quarters.

Use ranges rather than false precision. Never present scenario outputs or article
case studies as guarantees.
