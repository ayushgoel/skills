# Shared Company Evaluation

Use this framework to connect business evidence to prospective shareholder returns.
The identity is a tool for disciplined assumptions, not a claim that P/E always
describes economic value.

## Contents

1. Return identity
2. EPS engine
3. Valuation engine
4. Promoter and insider signal
5. Scenario construction
6. Decision matrix
7. Source and evidence discipline

## 1. Return identity

For positive, representative earnings:

```text
Price = diluted normalized EPS * P/E

Price CAGR =
  (1 + EPS CAGR) * (exit P/E / entry P/E)^(1 / years) - 1
```

Model buybacks through the diluted share count and resulting EPS; do not add the
same buyback again as cash yield. Separate these outputs:

- EPS CAGR;
- annualized multiple tailwind or headwind;
- price CAGR from their multiplicative combination;
- cumulative dividends per share;
- terminal-wealth CAGR, with dividends held as idle cash until exit;
- cash-flow IRR, with dividends received during the holding period.

Use cash-flow IRR for the default annual return hurdle. Its supported entry value
discounts each dividend at its payment time and the sale proceeds at exit. This
differs from discounting all dividend cash as if it arrived at the end. IRR does
not specify a reinvestment rate; a terminal-wealth calculation must state one if
dividends are reinvested. Disclose the calculator's year-end payment convention
and use dated cash flows when payment timing is material.

Do not use this identity with negative, near-zero, or unrepresentative EPS. Avoid
mixing trailing EPS with a forward multiple or double-counting forecast growth.

## 2. EPS engine

Rate the engine `strong`, `neutral`, `weak`, or `uncertain`, with a confidence level.
Support the rating with a multi-year record and forward evidence.

### Growth and durability

- Reconcile revenue, operating profit, net income, and diluted EPS growth.
- Separate volume, price/mix, acquisitions, currency, tax, interest, and share-count
  effects.
- Test whether the addressable market, competitive position, capacity, distribution,
  and customer economics can sustain the assumed duration.
- Apply the law of large numbers as an explicit forecast constraint, not as proof
  that growth must stop.

### Economics of reinvestment

Use this consistency check when data permits:

```text
fundamental operating growth ~= reinvestment rate * incremental return on capital
```

Examine incremental ROIC/ROCE rather than relying only on average ROE. Determine
whether ROE improvement comes from operating economics, leverage, shrinking equity,
buybacks, or accounting changes. A moat matters when it produces observable pricing
power, retention, cost advantage, efficient growth, or resilience—not because the
label itself deserves a higher multiple.

### Earnings quality

Check:

- operating cash flow and free-cash-flow conversion;
- working-capital requirements and supplier/customer financing;
- maintenance versus growth capex;
- capitalized expenses, exceptional income, subsidies, and tax normalization;
- dilution, options, convertibles, and minority interests;
- acquisition accounting and recurring restructuring adjustments;
- debt maturities, interest coverage, covenants, and contingent liabilities;
- cyclicality, seasonality, commodity exposure, and peak-margin risk.

Use normalized diluted EPS. Show both reported and normalized figures when the
reconciliation materially affects the thesis.

Show a reconciliation from reported profit attributable to common shareholders,
through one-offs and sustainable operating adjustments, to diluted EPS. Keep
the trailing and forecast periods explicit. A price divided by a vendor's P/E
is a consistency check, not a verified normalized EPS record. Reconcile company,
exchange and vendor discrepancies before using a number to justify an action.

Use profit attributable to owners of the parent, not total consolidated PAT
including non-controlling interests. Reconcile the filing's EPS numerator and
weighted-average diluted denominator after rights issues, bonuses, splits and
mergers. Dividing trailing owner profit by today's diluted share count is a useful
current-share-count diagnostic, but is not reported EPS or a completed earnings
normalization. Do not silently replace a conflicting filing or call the diagnostic
sustainable EPS. Keep material unreconciled differences as an evidence gap.

Bridge management-adjusted EBITDA and "cash PAT/profit" to statutory results.
Deferred-tax and depreciation add-backs do not demonstrate cash collection;
operating cash flow also reflects working capital and cash taxes. Separate operating
revenue from other income and remove non-operating fair-value or disposal gains
with their tax and minority-interest effects. Do not routinely add back credit
losses, liquidated damages or restructuring expenses that recur in the business.

For "net cash" or "debt-free" claims, check the reporting entity and date. Include
material supplier financing, leases, redeemable instruments and other debt-like
obligations, stating the chosen definition. Separate freely usable cash from
pledged deposits, earmarked issue proceeds and investments with uncertain liquidity;
do not offset all investments against debt without checking availability.

### Recovery and cyclicality

Identify whether weak earnings reflect a temporary shock, investment phase,
cyclical trough or structural deterioration. Build the recovery from volume,
capacity/utilization, margins, interest, taxes and diluted shares. Test the funding
needed to survive a delay. Do not perpetuate a trough indefinitely by default or
restore peak margins without evidence. For recovery cases, model year-by-year
cash flows when a constant EPS CAGR hides the path or funding risk.
Distinguish near-term revenue lost to a lower-scope product mix from weaker demand,
and quantify whether the new model actually improves margins, collections and
capital employed. Seasonal weakness is not proof of failure; repeatedly deferred
guidance without operational progress is not proof of an imminent recovery.

## 3. Valuation engine

Rate valuation `tailwind`, `neutral`, `headwind`, or `uncertain`. Do not call a stock
cheap merely because its multiple fell or is below a market average.

### Explain the multiple

Connect the valuation range to:

- expected growth and the duration of excess returns;
- incremental returns and reinvestment needs;
- free-cash-flow conversion and capital intensity;
- cyclicality and earnings quality;
- balance-sheet, governance, regulatory, customer, and country risk;
- interest rates and the required return;
- dividends, buybacks, and other capital returns.

Compare the current valuation with appropriate peers and the company's own history
only under comparable growth, margin, risk, and rate regimes. Use reverse valuation
where practical: state what growth, margin, and duration the market price appears to
require.

### Choose the right lens

| Business | Preferred starting lens | Required companion checks |
| --- | --- | --- |
| Profitable, stable operating company | Normalized P/E or FCF yield | Growth, risk, reinvestment, cash conversion |
| Bank or lender | P/B and justified P/B | Sustainable ROE, credit cost, capital adequacy, asset quality |
| Insurer | P/embedded value or suitable sector metric | New-business margin, persistency, solvency |
| Commodity or deep cyclical | Mid-cycle earnings or EV/EBITDA | Cycle position, replacement cost, balance sheet |
| Loss-making growth company | EV/revenue or unit economics | Path to margin and cash flow, dilution, funding runway |
| Capital-intensive company | EV/EBITDA and DCF/FCFF | Maintenance capex, debt, incremental ROIC |
| Conglomerate | Sum of the parts | Holding-company discount, cross-holdings, taxes |

Use enterprise-value measures when cash and debt materially distort equity multiples.
Use more than one method when model risk is high.

Document the source and economic rationale for exit valuations. Compare relevant
peers and the company's history under comparable rates and growth, rather than
arbitrarily choosing a multiple that makes the return pass.

## 4. Promoter and insider signal

Promoters can possess superior information and an aligned owner-operator can be an
important advantage. An increase in reported promoter percentage is not, by itself,
proof that insiders invested new money or that earnings will grow.

### Establish what happened

For every material change, report:

- promoter/person acting in concert and relationship to management;
- absolute shares and percentage before and after;
- transaction date, price, value, and mode;
- change in total diluted shares outstanding;
- transaction value relative to the promoter's existing holding and, when available,
  disclosed compensation or resources;
- source of funds and whether shares or other assets were pledged;
- subsequent sales, transfers, dilution, or encumbrance;
- current aggregate promoter pledge and its direction.

Use official exchange or regulatory disclosures. Cross-check quarterly shareholding
patterns against transaction filings. A percentage can rise passively after a company
buyback even when the promoter buys nothing.

### Classify the mechanism

| Signal | Typical evidence |
| --- | --- |
| Strong positive | Material open-market purchase at prevailing prices using promoter capital; meaningful commitment; no offsetting sale, dilution, or new pledge |
| Moderate positive | Rights participation or fairly priced allotment that commits meaningful capital and preserves alignment, with a credible use of funds |
| Neutral/ambiguous | Buyback-driven percentage increase, inheritance, gift, inter-se transfer, merger, reclassification, tiny purchase, or transaction without clear economics |
| Negative | Material open-market sale without a benign explanation, rising pledge/encumbrance, forced sale, repeated value-destructive dilution, or purchase funded through risky leverage |
| Unknown | Filing or transaction mechanism cannot be verified |

Explain rather than mechanically score. Consider alternative motives such as control,
takeover defense, minimum holding requirements, tax, family settlement, or liquidity.
Insider conviction can support an EPS-engine thesis, but operating results and
valuation must independently support the decision.

For pledges, distinguish percentage of promoter holding from percentage of total
equity. Investigate amount, trend, collateral purpose, financing entity and
forced-sale triggers. Mark unverified terms as unknown; a pledge percentage alone
does not establish fraud or prove that financing risk is immaterial.

## 5. Scenario construction

Use at least bear, base, and bull cases over the user's horizon. Make scenarios
internally consistent rather than changing only the exit multiple.

For each scenario state:

- revenue and normalized diluted EPS CAGR;
- margin, reinvestment, incremental return, and share-count assumptions;
- exit multiple and why it fits that scenario's growth, risk, and rates;
- next annual dividend per share and dividend growth when material;
- terminal price, price CAGR, cumulative dividends, terminal-wealth CAGR and IRR;
- probability only when evidence supports a calibrated estimate.

Run `../scripts/project_returns.py` for P/E-based cases. Use explicit DCF or the
appropriate sector method when P/E is invalid. Do not force incompatible valuation
methods into the calculator.
If normalized earnings or an exit multiple cannot yet be underwritten, a terminal
EPS/multiple sensitivity may expose what the price requires. Label it illustrative,
not a validated base case, forecast, downside floor or actionable buy zone. An
equivalent CAGR calculated backward from terminal EPS does not establish a recovery
path; connect any actionable case to annual operating drivers and funding needs.

Pass percentage inputs as percentage points (`15` means 15%, not `0.15`):

```json
{
  "current_price": 1000,
  "current_eps": 20,
  "horizon_years": 5,
  "hurdle_rate_pct": 12,
  "scenarios": [
    {
      "name": "Base",
      "eps_cagr_pct": 15,
      "exit_multiple": 32,
      "next_annual_dividend": 5,
      "dividend_cagr_pct": 15
    }
  ]
}
```

Run `python3 scripts/project_returns.py <input.json>` from the skill directory.
`next_annual_dividend` is the year-one dividend per share, paid at year-end in the
model. The calculator reports cash-flow IRR and terminal-wealth CAGR with no
dividend reinvestment. `hurdle_rate_pct` is optional; when present, the supported
entry price is the discounted value of yearly dividends and terminal proceeds,
consistent with cash-flow IRR. Treat it as a scenario diagnostic, not a target.

Stress-test:

- slower growth plus margin normalization;
- multiple compression without thesis failure;
- higher rates or risk premium;
- dilution, debt refinancing, or regulatory change;
- the growth required merely to offset plausible multiple compression.

For an unspecified hurdle, disclose the assumption and compare nearby required
returns. For a close call, vary growth and exit valuation over evidence-backed
ranges and calculate the growth required at the current price. A difference of
one percentage point in modeled return may be smaller than estimation error;
do not present it as certainty or reduce the hurdle merely to force a purchase.
State why the assumed hurdle and uncertainty buffer fit the risks being tested;
do not mechanically discount a speculative target and call the result fair value.

## 6. Decision matrix

| EPS engine | Valuation engine | Default interpretation |
| --- | --- | --- |
| Strong | Tailwind or neutral | Add/Initiate candidate if downside and portfolio fit are acceptable |
| Strong | Headwind | Hold, Trim, or Watch depending on expected return and concentration |
| Weak | Apparent tailwind | Possible value trap; require evidence of stabilization |
| Weak | Headwind | Exit/Avoid candidate unless a credible, underwritten turnaround exists |
| Uncertain | Any | Watch or use a small research position; demand a wider margin of safety |

First rate company merit against the return hurdle, then let portfolio-analysis
apply holdings, tax and allocation constraints:

- `Add/Initiate`: base return clears the hurdle with acceptable permanent-loss risk.
- `Hold`: prospective return remains adequate, but the margin of safety or incremental
  opportunity is insufficient to add.
- `Trim`: prospective return has fallen, valuation or concentration risk is high, or
  a superior risk-adjusted alternative exists.
- `Exit/Avoid`: the thesis is broken, governance or solvency risk is unacceptable, or
  prospective return is inadequate across plausible cases.
- `Watch`: missing evidence or wide outcomes prevent a responsible action.

Cost basis is not evidence of value. Use it only for tax, liquidity, and realized-loss
considerations. Never issue an action solely because price rose or fell by a threshold.

## Company Findings Contract

Use the same findings for a discovery finalist and an existing holding:

- identifier, price/as-of date and current classification;
- multi-year operating record and reported-to-normalized per-share reconciliation;
- earnings basis (`reported`, `current-share-count diagnostic`, `normalized` or
  `provisional`), consolidation perimeter and unresolved reconciliation items;
- EPS-engine and valuation-engine ratings with high/medium/low confidence;
- accounting, cash conversion, maintenance capex, leverage and funding risks;
- promoter transactions, pledge terms/trend and verified capital allocation;
- sector valuation lens, peer comparison and bear/base/bull driver assumptions;
- return decomposition, hurdle sensitivity, reverse valuation and entry range;
- thesis, next catalyst, operating KPIs and explicit invalidators;
- liquidity/evidence limits on starter and maximum size;
- research state and dated primary sources, distinguishing estimates and unknowns.

The caller supplies quantities and cost details separately. If evidence is missing,
state which conclusions remain unvalidated. A compact holdings review may group
small positions, but do not imply full underwriting where only triage was done.
Keep source dates, assumptions and review triggers with the findings so the portfolio
caller can reuse them without silently upgrading confidence or refreshing only price.

## 7. Source and evidence discipline

Use an explicit as-of date. Prefer:

1. exchange and regulator filings;
2. audited annual reports and filed quarterly results;
3. company presentations and call transcripts;
4. official industry or government data;
5. reputable secondary research for context.

For Indian promoter analysis, use current NSE/BSE corporate filings, SEBI disclosures,
and company filings. Transaction disclosures identify the mode—such as open market,
rights issue, preferential allotment, or inter-se transfer—which is essential to the
signal. Verify that a historical article or screen has not mixed split-adjusted and
unadjusted EPS or prices.

Label each material statement as reported fact, analyst estimate, management guidance,
or inference. State conflicting figures and unresolved gaps. Avoid precise return
promises, undocumented fair multiples, and unsupported claims about investor motives.

For analyst consensus, record provider, analyst count, observation dates and visible
methodology. A unanimous rating may be stale or cover few analysts; distinguish it
from the platform's own scorecard and technical signals. Do not invent gated targets,
and use direct business peers rather than a vendor's broad industry basket.
