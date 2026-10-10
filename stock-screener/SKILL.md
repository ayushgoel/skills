---
name: stock-screener
description: >-
  Screen a defined stock universe for investment opportunities, or evaluate named
  companies using current evidence, normalized fundamentals, sector-appropriate
  valuation, governance, liquidity and scenario returns. Use for stock discovery,
  buy zones, recovery and catalyst research, or the company evaluations delegated
  by portfolio-analysis. Portfolio reconciliation and allocation belong to
  portfolio-analysis.
---

# Stock Screener

Find credible opportunities and explain the expectations embedded in their prices.
Maintain one company-evaluation method for discovered stocks and existing holdings.

## Modes And Ownership

- **Screen opportunities:** read
  [references/opportunity-screening.md](references/opportunity-screening.md), build
  an auditable candidate funnel, then evaluate finalists with the shared evaluator.
- **Evaluate companies:** read
  [references/company-evaluation.md](references/company-evaluation.md) completely
  before rating named stocks. A request from portfolio-analysis uses this mode;
  it does not trigger discovery beyond the supplied holdings.
- For turnarounds, order books, capacity expansion, recovery or other catalyst-led
  theses, also read
  [references/catalyst-watchlist-framework.md](references/catalyst-watchlist-framework.md).

The screener owns company merit and research evidence. Portfolio-analysis applies
holdings, fund look-through, taxes and allocation constraints to those findings.
When both tasks are requested, share the evidence instead of independently
recalculating company value. No separate evaluator skill is required.

## Working Method

1. Establish the as-of date, universe, currency, horizon, budget and required
   return. Preserve explicit exclusions; distinguish hard restrictions from soft
   preferences. If the hurdle or order size is absent, disclose an illustrative
   assumption and show sensitivity instead of treating it as the user's mandate.
2. Verify current universe membership, identifiers and price dates. In India,
   BSE trading groups, index membership, AMFI size bands and F&O eligibility are
   separate attributes. None alone certifies business quality or manipulation.
   Use a current official list for a requested universe or exclusion.
3. In discovery mode, maintain counts and reasons through eligibility, quantitative
   triage and company research. Separate unknown data from rejection. Examine
   sector-specific value, durable growth and recovery/catalyst paths; a few
   familiar names cannot establish that a large universe has no opportunities.
4. Evaluate operating quality, normalized per-share earnings, governance, funding,
   cash conversion and the appropriate valuation lens. Reconcile material
   differences between reported and normalized earnings with dated sources.
   Separate firm backlog from optional pipeline and management-adjusted metrics
   from statutory earnings and cash flows using the relevant references.
5. Model bear, base and bull outcomes. For representative positive EPS, run
   `scripts/project_returns.py` from this skill using a temporary JSON outside the
   source repository. Report price CAGR, cash-flow IRR, terminal-wealth CAGR and
   dividend assumptions separately. The cash-flow IRR and its discounted entry
   value are the default comparison with an annual return hurdle.
6. Show growth, margin, exit-valuation and hurdle sensitivity for close calls.
   Reverse the valuation to expose what the price requires. Keep unsupported
   recovery or rerating in an upside scenario, rather than adjusting assumptions
   until a desired stock passes.
7. Rank investment merit before assessing portfolio suitability. An attractive
   stock can remain shortlisted with a zero suggested allocation because of
   existing exposure. Use states `Discover`, `Validate`, `Starter`, `Scale/Add`,
   `Hold`, `Trim` and `Exit/Archive`; distinguish research rejection from a sell
   decision on an existing holding. State confidence and evidence that changes it.
   Keep eligibility exclusions separate: an excluded or unreviewed security has
   no assessed company state, rather than an `Exit/Archive` investment judgment.

## Decision Discipline

- Verify a claim such as "multi-year low" for the specified index or stock and
  distinguish price drawdown from valuation and normalized earnings. Index-level
  P/E is context, not a reason to reject every constituent.
- Use liquidity on all relevant trading venues over a stated multi-week window,
  with spread/free-float checks and realistic order participation. One day on one
  exchange and a fixed market-cap floor do not establish investability.
- Investigate pledge amount, denominator, trend, purpose, collateral and financing
  stress. Do not turn every pledge into a fraud finding or overlook forced-sale
  risk because earnings look attractive.
- Allow an evidence-backed, capped starter when uncertainty is measurable and
  survivable. Stronger operating and cash-flow confirmation is normally needed
  before scaling; waiting for all uncertainty to disappear is not an entry rule.
- Present a ranked watchlist when no immediate buy is validated. Do not manufacture
  five buys or claim that no opportunity exists in an incompletely researched
  universe. Disclose missing evidence and the next research step.
- A prior rally or decline is a reason to audit assumptions and timestamps, not
  proof of the original thesis. Acquisition cost is relevant to taxes, not value.
- A platform's buy consensus or favourable entry indicator is a research lead,
  not evidence of intrinsic value. Verify what the signal measures, its date and
  coverage; do not treat technical entry conditions as fundamental cheapness.

## Output

For discovery, include:

- dated mandate and universe sources, funnel counts, sector coverage and data gaps;
- an eligibility/research ledger with identifiers, state, reason, dates and links;
- ranked company findings with normalized record, valuation lens, bear/base/bull
  returns, sensitivity, buy range, confidence, catalyst and invalidators;
- liquidity/order-size limits and governance/funding risks;
- rejected finalists and near misses with their decisive reasons;
- portfolio suitability as a separate column when holdings are known.

For named-company evaluation, return the company findings to the caller without
creating an unrelated candidate funnel or allocation plan. Missing primary data
means `Discover` or `Validate`, not a fabricated high-confidence rating.
Evaluate an explicitly requested company even when it is outside the new-buy
universe, but flag its eligibility separately; the request is not permission to
relax purchase restrictions. Keep research state separate from the caller's
decision to hold, add to or sell an existing position.

Keep generated reports, ledgers, input data and downloaded evidence beside a
user-supplied input or in a private temporary workspace. They do not belong in
this public skill repository. Use ranges for decisions; calculator precision is
not forecast precision.
