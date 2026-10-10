# Opportunity Screening And Coverage

Use this framework for discovery across the requested universe. Include mid caps
deliberately when relevant, without restricting every mandate to one size band.

## 1. Define the investable universe

- Build the requested universe from its dated official membership source. Use the
  current official Indian market-cap classification when a size band is in scope;
  do not substitute an index for an exchange group or hardcode stale rupee cutoffs.
- Record universe source, date, eligible security classes and hard/soft exclusions.
  Deduplicate economic securities by ISIN or verified identifiers, not approximate
  name matching. Resolve renamed tickers and unmatched cross-exchange mappings.
- Include the user's index and fund exposure when it is known. Show overlap and
  portfolio suitability after rating investment merit; overlap alone is not a
  reason to erase an attractive company from the shortlist.
- Check free float, median traded value over a stated multi-week window, bid-ask
  spread when available, delivery volume, and promoter/public ownership. Combine
  relevant NSE/BSE activity for dual-listed Indian stocks. Compare the intended
  order and exit plan with realistic turnover participation; justify any limit.
  Calculate the combined median from matched daily venue totals. The sum of
  separate venue medians is only a proxy and must be labeled as such.
  One exchange's single-session turnover or a fixed rupee market-cap floor is not
  sufficient to reject a small order. Missing liquidity evidence is a data gap.
- State whether the company entered the mid-cap band through business compounding,
  price rerating, demerger, or falling from a larger band. Classification is context,
  not evidence of quality.

## 2. Build a candidate funnel

Search beyond current holdings and familiar index constituents. Start with business
evidence, then valuation; do not rank on recent price CAGR.

Maintain a CSV or structured ledger outside the skill repository with security
identifier, sector, universe date/source, eligibility, triage status, evidence
status, decision reason, research state and source links. Report:

| Stage | Required accounting |
| --- | --- |
| Raw universe | Dated membership and duplicate/security-class removals |
| Eligible | Each exclusion and unmatched identifier |
| Triage | Sector-appropriate metrics, missing data and reason for each result |
| Research | Which companies were actually underwritten and which remain unreviewed |
| Finalists | Actionable ideas, near misses, rejected theses and unresolved evidence |

Counts must reconcile. Distinguish eligible, data-complete and researched counts.
Keep `excluded` as an eligibility result with its mandate reason, not an
`Exit/Archive` company state. Unreviewed names have no assessed investment merit.
Use full-universe quantitative triage when data permits; verify finalists against
primary sources. If access limits coverage, report the researched subset and
unreviewed remainder. Never infer "no opportunities in the universe" from a
handpicked list or silently treat missing data as a failed business.

Cover three paths rather than filtering every stock on the same trailing P/E:

1. Durable compounders with attractive reinvestment economics and cash conversion.
2. Value/income businesses with sustainable normalized cash returns.
3. Recovery/catalyst businesses with a measurable change and survivable funding.

Check sector variety and investigate promising omissions. An index's aggregate
valuation or a general concern about small caps does not reject every constituent.

Prefer candidates showing several of these traits:

- a five-to-ten-year addressable runway with low current penetration;
- demonstrated volume or customer growth rather than price-led revenue alone;
- incremental ROIC/ROCE above the cost of capital and stable or improving unit economics;
- capacity or distribution investment that is funded and approaching utilization;
- operating cash flow that reconciles with earnings across a cycle;
- room for market-share gains without assuming implausible industry dominance;
- a balance sheet capable of surviving delays, rate shocks, and one weak cycle;
- owner-operator alignment with clean related-party conduct and limited pledging;
- a valuation where base returns are carried mainly by per-share fundamentals.

Maintain sector variety in the research funnel, but never lower the quality bar to
manufacture diversification.

## 3. Separate rejection from uncertainty

Reject or label speculative when material evidence establishes an unacceptable
risk that cannot be resolved:

- auditor resignation, repeated qualified opinions, opaque subsidiaries, or material
  related-party leakage;
- promoter pledging or leverage that can force equity sales;
- reported profit persistently unsupported by operating cash flow without a credible
  working-capital explanation;
- serial dilution, warrants, or acquisitions that prevent per-share compounding;
- customer, supplier, geography, or product concentration without adequate resilience;
- debt-funded capex whose base case requires perfect utilization or refinancing;
- insufficient filings, conference-call evidence, or liquidity for responsible sizing.

Unknown evidence belongs in `Discover`/`Validate`, with the next verification
named. Investigate pledges and temporary working-capital absorption in context;
do not mechanically reject a company for any encumbrance or one weak quarter.

Promoter open-market buying can strengthen a passing thesis. It cannot repair a failed
governance, earnings-quality, or valuation gate.

## 4. Underwrite the runway

Create an explicit driver tree:

```text
Revenue = addressable market * reachable share * price/mix
Operating profit = revenue * normalized margin
Per-share earnings = normalized profit attributable to common equity / diluted shares
```

For each driver, distinguish reported history, management guidance, outside estimate,
and inference. Test capacity, utilization, distribution, customer wins, input costs,
working capital, maintenance capex, tax, interest, and dilution. Use incremental returns
on new capital—not only the historical average ROE.

Mid-cap growth often fails through duration rather than direction. Model how long high
growth can persist before competition, base effects, capacity, regulation, or customer
concentration cause normalization.

## 5. Require a mispricing thesis

State what the market may be getting wrong. Valid possibilities include temporary
margin compression, an investment phase before utilization, a misunderstood segment,
balance-sheet repair, a credible governance improvement, or earnings hidden by a
cyclical trough. A low P/E, a fallen price, or an exciting industry is not enough.

Use reverse valuation to expose the expectations already embedded in price. The base
case should clear the user's hurdle with a neutral or lower exit multiple. If it needs
rerating, classify it as a tactical or speculative case and size it accordingly.

## 6. Compare candidates consistently

Rank the shortlist on evidence rather than a mechanical score. Show at least:

| Dimension | Required question |
| --- | --- |
| Runway | Can per-share earnings plausibly compound for five years or more? |
| Incremental economics | Does new capital earn attractive incremental returns? |
| Cash conversion | Do operating cash flow and maintenance capex support reported EPS? |
| Balance sheet | Can the company self-fund the base case and survive the bear case? |
| Governance | Are ownership, pledges, dilution, auditors, and related parties acceptable? |
| Valuation | Does the base case work without optimistic multiple expansion? |
| Liquidity | Can the intended position be accumulated and exited responsibly? |
| Variant view | What is mispriced, and what evidence would prove the thesis wrong? |

Compare finalists with direct listed peers under the same normalization. Do not compare
raw multiples across different margins, capital intensity, growth duration, or leverage.

## 7. Size and stage entries

- Tie initial size to evidence quality, liquidity, governance, cyclicality, and bear-case
  permanent-loss risk—not expected upside alone.
- Use a research or starter position when the thesis awaits a measurable milestone.
- Increase only after evidence improves or price creates a wider margin of safety.
- Cap correlated mid-cap theses as a group; five small industrial suppliers can be one
  capex-cycle bet.
- State an entry range and the assumptions supporting it. Do not chase above the range
  because the price is rising.

## 8. Produce an auditable shortlist

For each finalist report the current classification, liquidity, thesis, mispricing,
normalized record, scenarios, buy range, staged size, catalyst sequence, risks, and
invalidators with dated sources. Also list serious candidates rejected at the final
gate and the decisive reason. This prevents a screen from silently becoming a list of
only attractive stories.

Separate `investment merit`, `evidence maturity`, `current entry attractiveness`
and `portfolio suitability`. A strong idea can have no suggested allocation under
the user's restrictions. A near miss can remain a ranked watch rather than be
described as worthless. If nothing is actionable, state the coverage boundary and
whether the blocker is valuation, business risk, mandate or incomplete research.
