# Family Wealth Advisor — Reference Material

Cross-cutting reference material that applies regardless of income tier. See `references/tier-1-foundational.md` through `references/tier-5-legacy-planning.md` for tier-specific playbooks.

**Last verified: July 2026 (tax year 2026 figures, post-OBBBA).** All figures below are subject to annual IRS inflation adjustment and occasional legislative change — confirm current-year numbers before using them in any calculation that matters, per the skill's Tax Guidance Standard.

## Table of Contents
1. [Current-Year Key Thresholds](#current-year-key-thresholds)
2. [Backdoor Roth IRA Strategy & the Pro-Rata Rule](#backdoor-roth-ira-strategy--the-pro-rata-rule)
3. [Mega-Backdoor Roth: Mechanics and Limits](#mega-backdoor-roth-mechanics-and-limits)
4. [Whole Life Insurance Mechanics: 7-Pay Test, MEC Status, and PUA Riders](#whole-life-insurance-mechanics-7-pay-test-mec-status-and-pua-riders)
5. [Estate Tax Exemptions: Federal and State Landscape](#estate-tax-exemptions-federal-and-state-landscape)
6. [529 Plans: Contribution Mechanics, State Availability, and Tax Parity](#529-plans-contribution-mechanics-state-availability-and-tax-parity)
7. [Trump Accounts (IRC §530A): Custodial Accounts for Minors](#trump-accounts-irc-530a-custodial-accounts-for-minors)

---

## Current-Year Key Thresholds

The single consolidated source for the numbers referenced across SKILL.md and the tier files. Update this table annually rather than hunting through every file that mentions a threshold.

| Threshold | 2026 figure | Per person or per household? | Why it matters |
|---|---|---|---|
| Roth IRA MAGI phase-out (single/HoH) | $153,000–$168,000 | Household | Full contribution below $153,000; none above $168,000 — the Tier 1→3 boundary for single filers |
| Roth IRA MAGI phase-out (MFJ) | $242,000–$252,000 | Household — this *is* the joint figure; do not double it | Same mechanism for married filing jointly — the Tier 2→3 boundary used throughout this skill |
| IRA contribution limit | $7,500 ($8,600 with 50+ catch-up of $1,100) | **Per person** — each spouse has their own, including catch-up, even if one has no earned income (spousal IRA) | Direct or backdoor Roth/traditional IRA annual cap |
| 401(k)/403(b) employee deferral limit | $24,500 | **Per person** (aggregated across all of that person's plans) | Standard employee elective deferral |
| Section 415(c) overall defined-contribution limit | $72,000 | **Per person, per unrelated employer plan** | Combined employee + employer + after-tax contributions to a single employer plan — the ceiling that makes mega-backdoor Roth and SEP-IRA/Solo 401(k) contribution room possible (see [Mega-Backdoor Roth](#mega-backdoor-roth-mechanics-and-limits)) |
| HSA contribution limit (self-only / family) | $4,400 / $8,750 (+$1,000 catch-up at 55+) | Household for the family limit; the catch-up is **per person** and requires each spouse to have their own HSA to use it | Available if enrolled in a qualifying HDHP, regardless of tier |
| NIIT threshold (single/HoH, MFJ, MFS) | $200,000 / $250,000 / $125,000 | Household | Fixed by statute since 2013, **not** inflation-indexed — the Tier 2→3 boundary alongside the Roth phase-out; triggers an additional 3.8% tax on net investment income above the threshold |
| Top federal bracket (37%) threshold (single, MFJ) | $640,600 / $768,700 | Household | The Tier 3→4 boundary — "peak accumulator" territory |
| QBI/Section 199A SSTB phase-out (MFJ) | Begins ~$403,500, phase-out window ~$150,000 wide (fully phased out by ~$553,500) | Household | Relevant to self-employed SSTB business owners (consulting, law, medicine, financial services, etc.) — sources vary slightly on the exact figures post-OBBBA; confirm against the current-year IRS Revenue Procedure before relying on an exact number |
| Saver's Credit AGI limits (single/MFS/QSS, HoH, MFJ) | $40,250 / $60,375 / $80,500 | Household | Relevant at Tier 1 — note that 2026 is the final year of the Saver's Credit in its current form; it's replaced by the "Saver's Match" starting tax year 2027, which works differently (a direct contribution to the saver's retirement account rather than a tax refund credit) — check whether this skill's Tier 1 guidance needs updating once that transition happens |
| Standard deduction (single / MFJ) | $16,100 / $32,200 | Household (MFJ figure shown) | Determines whether itemizing is worthwhile — the gate on charitable bunching strategies |
| Trump Account (IRC §530A) annual contribution limit | $5,000 per child, aggregate | **Per child** — combines individual, employer, and cafeteria-plan contributions from all sources into one shared cap | Not indexed for inflation until after 2027; see [Trump Accounts](#trump-accounts-irc-530a-custodial-accounts-for-minors) |
| Trump Account federal seed contribution | $1,000 per eligible child, one-time | Per child — does **not** count against the $5,000 annual limit above | Only for U.S.-citizen children born 1/1/2025–12/31/2028; requires an affirmative election on Form 4547 |
| Federal estate tax exemption | $15,000,000 per individual | **Per person** — portable to a surviving spouse with a timely filed election, giving $30,000,000 per couple | Made permanent and indexed going forward by the One Big Beautiful Bill Act (OBBBA), signed July 2025 — a large increase from the pre-OBBBA 2025 figure of $13.99M; see [Estate Tax Exemptions](#estate-tax-exemptions-federal-and-state-landscape) for why state exemptions matter far more than this federal number for most Tier 5 conversations |
| Annual federal gift tax exclusion | $19,000 per recipient | **Per donor, per recipient** — a married couple can give $38,000 to the *same* recipient | Relevant to lifetime gifting strategies at Tier 5, and the governing constraint on annual 529 funding (see [529 Plans](#529-plans-contribution-mechanics-state-availability-and-tax-parity)) |
| State income tax deduction for 529 contributions | Varies by state | **Almost always household** — a state's "MFJ" cap is already the joint figure and does *not* double | The most commonly misapplied figure in this table; see the 529 section |

**Before applying any threshold to a married household, read the middle column.** Roughly half of these figures double for a couple and half do not, and which is which is not predictable from the nature of the threshold. The pattern is that limits attached to *a person* (contribution limits, exclusions, exemptions) generally double, while limits attached to *a tax return* (income phase-outs, bracket thresholds, deduction caps) generally do not. State deduction caps are the most frequent source of error: they are attached to the return, are usually quoted as an MFJ figure already, and do not double.

### Sources
- [401(k) limit increases to $24,500 for 2026, IRA limit increases to $7,500 (IRS)](https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500)
- [IRS releases tax inflation adjustments for tax year 2026, including OBBBA amendments (IRS)](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill)
- [Net Investment Income Tax (Topic 559, IRS)](https://www.irs.gov/taxtopics/tc559)
- [IRS Notice 2026-05 — HSA and HDHP limits](https://www.irs.gov/pub/irs-drop/n-26-05.pdf)
- [Roth IRA income limits for 2026 (CNBC, summarizing IRS guidance)](https://www.cnbc.com/2025/11/13/roth-ira-income-limits-2026.html)
- [2026 Tax Brackets and Federal Income Tax Rates (Tax Foundation)](https://taxfoundation.org/data/all/federal/2026-tax-brackets/)
- [The Estate Tax Exemption Amount for 2026 (Kiplinger)](https://www.kiplinger.com/taxes/new-estate-tax-exemption-amount)
- [Saver's Credit: How to claim it in 2025 and 2026 (Fidelity)](https://www.fidelity.com/learning-center/smart-money/savers-credit)

---

## Backdoor Roth IRA Strategy & the Pro-Rata Rule

### Context & Core Mechanism
The "Backdoor Roth" is a multi-step strategy used by high earners to fund a Roth IRA when their modified adjusted gross income (MAGI) exceeds the legal threshold for direct contributions. It relies on making a **non-deductible (after-tax) contribution** to a Traditional IRA, followed immediately by a **conversion** of those funds into a Roth IRA.

However, the strategy depends entirely on minimizing the tax liability of the conversion step. This tax liability is governed by the IRS **Pro-Rata Rule** under Internal Revenue Code (IRC) Section 408(d), which mandates that any distribution or conversion from an IRA must consist of a proportional mix of pre-tax and after-tax dollars across **all** non-Roth IRA accounts.

### The December 31st Balance Requirement
A common misconception is that the taxability of a conversion is determined by the account balances on the day the conversion takes place. In reality, **the IRS measures the total balance of your aggregated IRAs at midnight on December 31st of the calendar year in which the conversion occurs.**

Under the **IRA Aggregation Rule**, the IRS treats all of an individual's non-Roth IRAs as a single, combined pool of capital. This includes:
* Traditional IRAs
* Rollover IRAs
* SEP-IRAs
* SIMPLE IRAs

*Note: Employer-sponsored plans (like standard 401k, 403b, or 457b accounts) and Inherited IRAs are excluded from this aggregation pool.*

#### The Calculation Formula
The tax-free portion of a Roth conversion is calculated using the formula found on **IRS Form 8606 (Line 6 through Line 10)**:

$$\text{Tax-Free Portion \%} = \frac{\text{Total After-Tax Contributions (Basis)}}{\text{Total Balance of ALL Aggregated non-Roth IRAs on Dec 31st} + \text{Current Year Conversions/Distributions}}$$

If your aggregate Traditional, SEP, and SIMPLE IRA balances are not exactly **$0.00** on December 31st, a portion of your conversion will be retroactively subjected to ordinary income tax, nullifying the advantage of a clean backdoor contribution.

### Common Timing Traps
1. **The Late-Year Rollover:** A user completes a clean $7,000 backdoor conversion in February when their IRA balance is zero. In October of that same calendar year, they change jobs and roll a $100,000 pre-tax 401(k) into a Traditional Rollover IRA. On December 31st, their aggregate IRA balance is $100,000. The February conversion is now subject to the Pro-Rata rule, triggering a retroactive tax bill.
2. **Delayed Clearance:** Attempting to clear out a pre-tax IRA near the end of December. If processing delays push the final transfer or reverse-rollover past midnight on December 31st, the snapshot will capture the lingering pre-tax funds.

### Mitigating Strategies to Achieve a Zero Balance
* **The "Reverse Rollover":** Roll any pre-tax Traditional, Rollover, SEP, or SIMPLE IRA balances into an active employer 401(k) or 403(b) plan. Because workplace 401(k) balances do not count toward the IRA aggregation calculation, this removes them from the Pro-Rata equation.
* **Full Conversion & Tax Settlement:** If the pre-tax balance is negligible (e.g., accrued interest or small legacy balances), convert the entire amount to the Roth IRA alongside the backdoor contribution and pay ordinary income tax on the pre-tax portion to establish a permanent $0 basis moving forward.
* **Solo 401(k) Transition:** For users with valid self-employment income, opening a Solo 401(k) provides an eligible refuge for pre-tax IRA funds that shields them from the Pro-Rata calculation.

### Official IRS Documentation References
* **IRS Form 8606 (Nondeductible IRAs):** Lays out the step-by-step reporting lines. Line 6 specifically demands the fair market value of all IRAs as of December 31.
  * [Official Landing Page](https://www.irs.gov/forms-pubs/about-form-8606)
  * [Form 8606 PDF Form](https://www.irs.gov/pub/irs-prior/f8606--2024.pdf)
  * [Form 8606 Instructions PDF](https://www.irs.gov/pub/irs-pdf/i8606.pdf)
* **IRS Publication 590-B (Distributions from IRAs):** Explains the underlying statutory logic under the "Prorating Only Nondeductible Contributions" section.
  * [Official Landing Page](https://www.irs.gov/forms-pubs/about-publication-590-b)
  * [Publication 590-B Full Web Guide](https://www.irs.gov/publications/p590b)
  * [Publication 590-B PDF Version](https://www.irs.gov/pub/irs-pdf/p590b.pdf)

---

## Mega-Backdoor Roth: Mechanics and Limits

### Core Mechanism
The mega-backdoor Roth is a Tier 4 strategy that goes well beyond the standard $7,500 IRA-based backdoor Roth. It uses the much larger **Section 415(c) annual additions limit** ($72,000 for 2026) that applies to an employer's defined-contribution plan (401(k), 403(b), profit-sharing, or Solo 401(k)).

The mechanism has two required steps:
1. **After-tax contributions to the 401(k), beyond the standard pre-tax/Roth employee deferral.** Many plans stop at the $24,500 employee deferral limit, but some allow additional *after-tax* (not Roth, not pre-tax — a third contribution type) contributions up to the overall $72,000 ceiling.
2. **In-plan Roth conversion or in-service withdrawal.** The after-tax contributions must be converted to Roth status — either via an in-plan Roth conversion (moving the after-tax bucket to the plan's Roth 401(k) bucket) or an in-service withdrawal to an external Roth IRA — ideally done promptly, since any earnings that accrue on the after-tax money before conversion are taxable at conversion, similar to the standard backdoor Roth's basis-tracking issue.

### The Available Space, Concretely
$$\text{Available mega-backdoor room} = \$72{,}000 - \text{employee deferral} - \text{employer match/contribution}$$

For 2026, if an employee maxes the standard $24,500 deferral and receives no employer match, up to **$47,500** of after-tax contribution room is theoretically available — but employer matching or profit-sharing contributions reduce this dollar-for-dollar. A household should get the actual number from their plan's contribution structure, not assume the full $47,500 is available.

### The Critical Gate: Plan Design
Unlike the IRA-based backdoor Roth (which any taxpayer can execute regardless of employer), the mega-backdoor Roth is entirely dependent on the specific 401(k) plan document. Many plans — especially at smaller employers — do not support after-tax contributions or in-plan conversion at all. **Always confirm with the plan administrator before assuming this is available**, rather than defaulting to "check with HR" as a vague action item — ask specifically: (1) does the plan accept after-tax (non-Roth, non-pre-tax) employee contributions, and (2) does it support in-plan Roth conversion or in-service withdrawals of those after-tax dollars. Solo 401(k) plans can often be structured by the plan provider specifically to support this from the outset, which is an advantage over adopting a generic off-the-shelf Solo 401(k) document.

### Common Pitfalls
* **Assuming it's unavailable without asking.** This is flagged in the Tier 4 reference file as a common miss — many employees never ask HR/the plan administrator whether after-tax contributions are supported, and skip a potentially large annual Roth-space lever as a result.
* **Letting after-tax contributions sit and accrue earnings before converting.** Earnings that accrue between the after-tax contribution and the Roth conversion are taxable at conversion — convert promptly (ideally automatically, if the plan supports "auto-convert" after-tax contributions).
* **Not accounting for employer contributions reducing available room.** The $72,000 ceiling includes employer money — a generous match or profit-sharing contribution can substantially shrink the after-tax space actually available.
* **Catch-up contributions do not increase the $72,000 limit** — the 415(c) ceiling is separate from the age-50+ catch-up allowance that applies to the employee deferral piece.

### Sources
- [401(k) limit increases to $24,500 for 2026, IRA limit increases to $7,500 (IRS)](https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500)
- [The 415(c) Annual Additions Limit, Explained](https://retirementcheck101.com/library/415c-annual-additions-limit.html)

---

## Whole Life Insurance Mechanics: 7-Pay Test, MEC Status, and PUA Riders

### The 7-Pay Test and Modified Endowment Contracts (IRC §7702A)
A life insurance policy that meets the general tax-law definition of life insurance (IRC §7702) still gets favorable tax treatment on cash-value growth and access — but only if it also passes the **7-pay test** under IRC §7702A, enacted by the Technical and Miscellaneous Revenue Act of 1988 (TAMRA).

The 7-pay test measures whether a policy is being funded too aggressively in its early years: if the cumulative premiums paid at any point during the first 7 contract years exceed what a level-premium schedule would require to pay up the policy in exactly 7 annual installments, the policy fails the test and becomes a **Modified Endowment Contract (MEC)**.

**Why this matters practically:** a policy funded with a large paid-up additions (PUA) rider — precisely the structure that makes whole life cash-value growth efficient (see below) — can inadvertently trip the 7-pay test if funded too aggressively too fast. This is a real design tension: PUA riders accelerate cash-value growth, but overfunding them in the early years risks MEC status.

**Consequence of MEC status:** loans and withdrawals from a MEC are taxed **gains-first** (any growth above basis is taxed as ordinary income before basis is considered untaxed), and withdrawals/loans taken before age 59½ can also trigger a 10% federal penalty on the taxable portion — eliminating the tax-free policy loan feature that is usually the main reason someone funds cash-value life insurance aggressively in the first place. MEC status is generally permanent for the life of the contract once triggered; it cannot be undone by later reducing premiums.

### Paid-Up Additions (PUA) Rider
A PUA rider allows additional premium dollars, beyond the base policy premium, to purchase small increments of fully paid-up additional coverage — each increment immediately adds both death benefit and cash value, without triggering additional ongoing premium obligations of its own. This is the standard mechanism insurance professionals use to make a whole life policy's cash-value accumulation more efficient than a "base-only" policy, since a higher proportion of each dollar goes toward cash value rather than the base policy's higher built-in cost structure and commission load.

**The tension to flag to a client:** a policy with a well-structured PUA rider is generally a better whole life product than a base-heavy policy with minimal PUA — but funding a PUA rider aggressively is exactly the kind of overfunding that can trip the 7-pay test and cause MEC status. A qualified agent/CFP structuring the policy correctly should be managing this tradeoff explicitly, and it's a fair question for a client to ask directly: "how does the funding schedule stay under the 7-pay limit while maximizing the PUA rider?"

### What to Ask For Before Any Purchase
- The **in-force illustration at guaranteed rates**, not just the projected/non-guaranteed dividend scenario — the guaranteed column is the only one that represents a contractual promise
- Explicit confirmation of **7-pay test compliance** and that the policy is not designed to become (or risk becoming) a MEC, unless MEC status is a deliberate choice for a specific goal
- The **commission structure** — whole life commissions are commonly front-loaded in the 50-100%+ of first-year-premium range, which is worth knowing when evaluating why a particular policy or funding schedule was recommended

### Sources
- [26 U.S.C. §7702A — Modified endowment contract defined](https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-prelim-title26-section7702A&num=0&edition=prelim)
- [The 7-Pay Test Under IRC Section 7702A: MEC Rules (LegalClarity)](https://legalclarity.org/the-7-pay-test-under-irc-section-7702a-mec-rules/)
- [What Is a Modified Endowment Contract Under IRC 7702A? (LegalClarity)](https://legalclarity.org/what-is-a-modified-endowment-contract-under-irc-7702a/)

---

## Estate Tax Exemptions: Federal and State Landscape

### Federal Exemption
The federal estate tax exemption is **$15,000,000 per individual ($30,000,000 per married couple)** for 2026, made permanent (and indexed for future inflation) by the One Big Beautiful Bill Act (OBBBA), signed July 2025 — a substantial increase from the pre-OBBBA 2025 figure of $13.99M. The federal exemption is portable between spouses (a surviving spouse can use a deceased spouse's unused exemption, with the correct election filed).

**Practical implication:** given how high the federal exemption now sits, most Tier 5 conversations in practice are actually driven by **state** estate or inheritance tax exposure, not federal — state exemptions are dramatically lower and, critically, many states do **not** offer spousal portability the way the federal system does.

### States With an Estate Tax (12 states + DC, as of 2026)
Connecticut, Hawaii, Illinois, Maine, Maryland, Massachusetts, Minnesota, New York, Oregon, Rhode Island, Vermont, Washington, and the District of Columbia.

Exemption amounts and cliff structures vary significantly by state and change periodically — do not assume a figure without checking the specific state. Some of these states (New York is a well-documented example) have an exemption **cliff**: if the estate exceeds the exemption by more than a small margin (commonly cited around 105% of the exemption in NY), the *entire* estate becomes taxable, not just the amount above the exemption — a materially different (and much harsher) mechanism than the federal system's marginal excess-only taxation.

### States With an Inheritance Tax (5 states, as of 2026)
Kentucky, Maryland, Nebraska, New Jersey, and Pennsylvania. Inheritance tax is levied on the recipient of an inheritance (with the rate commonly depending on the recipient's relationship to the deceased — spouses and children are typically exempt or taxed at the lowest rate, more distant relatives and unrelated beneficiaries at higher rates) rather than on the estate itself before distribution.

**Maryland is the only state that imposes both** an estate tax and an inheritance tax.

### Everywhere Else
The remaining ~34 states impose neither an estate tax nor an inheritance tax at the state level — for a household in one of those states, only the federal exemption is relevant, which given the current $15M/individual level means most households will never face estate tax exposure at all.

### Life Insurance and the Gross Estate

**A life insurance death benefit is included in the insured's gross estate**, for both federal and state purposes, when the insured owns the policy. This matters most for households that are *currently* comfortably below a state exemption, because the recommendation to buy term coverage can itself create the exposure — a household well under a state threshold can be pushed over it by the very policy intended to protect them. In a state with an exemption cliff, that converts the *entire* estate to taxable rather than just the excess, which can cost more than the coverage was ever worth.

Two further points that are easy to get wrong:

- **The exposure usually lands at the second death, not the first.** The unlimited marital deduction means a transfer to a surviving spouse is untaxed regardless of size. The estate to measure against the exemption is therefore the *survivor's*, which by then holds both spouses' assets plus any death benefit — and in states without portability, against a single exemption.
- **Sequence matters.** Where an irrevocable life insurance trust (ILIT) is warranted, the trust should be formed first and should apply for and own the policy from inception. Transferring an *existing* policy into an ILIT starts a three-year lookback under IRC §2035, during which the death benefit is still included in the estate.

**Whenever recommending life insurance, project the estate against the client's state exemption *including* the proposed death benefit before recommending an ownership structure.** This check costs one calculation and is routinely skipped.

### Why This Matters for Tier 5 Identification
A household's Tier 5 status should be checked against **both** the federal exemption and their specific state's rules (if any) — a $4M estate in a no-estate-tax state has no exposure at all, while the same $4M estate in a state with a lower exemption and a cliff (again, New York is the frequently cited example) may already be in taxable territory. Don't apply a single "$X net worth triggers Tier 5" rule of thumb across all households; the state of residence changes the answer materially.

### Sources
- [The Estate Tax Exemption Amount for 2026 (Kiplinger)](https://www.kiplinger.com/taxes/new-estate-tax-exemption-amount)
- [Where Not To Die In The U.S. In 2026 (Forbes)](https://www.forbes.com/sites/kellyphillipserb/2026/05/16/state-estate-inheritance-taxes-probate-costs-2026/)
- [16 States With Estate Taxes or Inheritance Taxes (AARP)](https://www.aarp.org/money/retirement/states-with-estate-inheritance-taxes/)
- [States With No Inheritance Taxes or Estate Tax in 2026 (Kiplinger)](https://www.kiplinger.com/taxes/states-with-no-inheritance-estate-tax)

---

## 529 Plans: Contribution Mechanics, State Availability, and Tax Parity

### There Is No Federal Annual Contribution Limit

This is the single most misunderstood feature of 529 plans, by clients and advisors alike. A 529 has no annual contribution cap in the way a 401(k) or IRA does. What people call "the limit" is really **four separate constraints**, and a household will typically be bound by a different one than they assume:

| Constraint | What it is | Doubles for a married couple? |
|---|---|---|
| **Annual gift tax exclusion** | $19,000 (2026) per donor, per beneficiary. Exceeding it is *legal* — it consumes lifetime exemption and requires Form 709 | **Yes** — two donors, so $38,000 to the same beneficiary |
| **Five-year gift-tax averaging ("superfunding")** | Front-load 5× the annual exclusion in one year, elected on Form 709 | **Yes** — $95,000 per donor, $190,000 per couple |
| **State income tax deduction cap** | Varies by state; commonly a few thousand to $10,000+ | **No** — a state's MFJ figure is already the joint number |
| **State aggregate balance cap** | Total balance per beneficiary across all of that state's accounts; commonly $300,000–$600,000 | **No** — per beneficiary, not per donor |

**Ask which of these the client has been targeting** (see "Never Accept 'We Max It Out' at Face Value" in SKILL.md). The most common pattern by far is a household anchoring to the *state deduction cap* — because that is the number the state's plan markets — while leaving the far larger federal gift exclusion unused. The state deduction is worth the cap multiplied by the state marginal rate, typically a four-figure annual sum. The federal benefit forgone is tax-free compounding on the difference, over the whole horizon to matriculation, which is routinely two orders of magnitude larger. Quantify both before concluding the client's practice is sensible.

### Superfunding: The Trade-Off to Quantify

Five-year averaging front-loads five years of exclusions into a single contribution, capturing compounding on the full amount immediately rather than in annual instalments. The cost is that in states which cap the deduction annually **with no carryforward of excess contributions**, the client forfeits the deduction in each of the averaging years in which they make no new contribution.

Do not present superfunding as unambiguously correct. Compute both paths — the additional balance from front-loading, against the state deductions given up — and present the net. Front-loading usually wins, but by a margin that is often small enough that a client who dislikes the five-year commitment or the Form 709 filing can reasonably contribute the full annual exclusion instead and capture most of the benefit. Either dominates anchoring to a state deduction cap; do not let the choice between them become a reason for delay.

### Aggregate Balance Caps Bind Before You Expect

The aggregate cap applies to *contributions*, not to subsequent market growth — an account may grow past the cap, but no further contributions are accepted while the balance sits above it. In a well-funded plan with a long horizon this frequently binds several years before matriculation, which means a household cannot simply contribute its way to full funding. Model the cap explicitly rather than projecting unconstrained contributions, and tell the client which years will need funding from outside the 529.

### K-12 Tuition: Check State Conformity Before Recommending It

Federal law permits 529 withdrawals for K-12 tuition, and the OBBBA raised the annual cap to **$20,000 per beneficiary beginning in 2026** (from $10,000). Against a large private school bill this looks compelling on its face.

**But a number of states never conformed to the K-12 provision** — New York is the most frequently cited example — and treat K-12 withdrawals as *non-qualified for state purposes*. The consequence is recapture of every state deduction previously claimed on that account, plus state income tax on the earnings portion of the withdrawal. For a household in a high-tax state with years of deductions behind it, that can turn an apparent saving into a real cost.

Never present the federal rule as if it settles the question. Check the specific state's conformity first, and if the state has not conformed, say so plainly and keep the 529 pointed at higher education.

### Overfunding Is Now Substantially Recoverable

SECURE 2.0 permits rolling up to **$35,000 lifetime** of leftover 529 funds into the beneficiary's own Roth IRA, subject to conditions (the account must generally have been open 15 years, the rollover is capped each year at the beneficiary's IRA contribution limit and requires earned income, and contributions from the preceding five years are ineligible). Raise this whenever a client hesitates to fund a 529 fully out of fear of overfunding — it does not eliminate the risk, but it materially reduces the downside of the most common objection to adequate funding.

### Availability
Every state plus the District of Columbia sponsors at least one 529 college savings plan, with one partial exception: **Wyoming terminated its own state-sponsored 529 plan in 2006** and does not currently offer one. This is not a practical obstacle for Wyoming residents, though, for two reasons: (1) Wyoming has no state income tax, so there was never a state-deduction incentive to use an in-state plan anyway, and (2) **you are generally not restricted to your own state's 529 plan** — nearly any state's plan can be opened by a resident of any other state, regardless of where you live. The only reason residency typically matters is whether your *home* state offers a tax deduction or credit tied to using its own plan (see below).

Because of this open-enrollment structure, the real decision for most families isn't "does my state have a 529 plan" — it's "does my state's tax treatment lock me into using its plan, or can I shop nationally for a better one (lower fees, better investment options) without losing a deduction."

### Three Categories of State Tax Treatment

**1. No state income tax (deduction question is moot).**
Alaska, Florida, Nevada, New Hampshire, South Dakota, Tennessee, Texas, Washington, and Wyoming have no broad-based personal income tax, so there's no state deduction to chase either way — residents of these states should simply pick the 529 plan with the best investment options and lowest fees nationally (common choices include Utah's my529 or Nevada's Vanguard 529, though this changes as plans compete on fees — check current comparisons rather than treating any specific plan as a permanent recommendation).

**2. Home-state-only deduction (the most common category).**
Most states with an income tax offer a deduction or credit for 529 contributions, but **only** if the contribution goes to that state's own plan. This is the category most families fall into, and it's why checking "does contributing to our home state's plan actually save us money on our state return, and if so, is the plan itself any good" is a standard part of the 529 conversation. New York's plan (referenced elsewhere in this skill, with a deduction up to $10,000/year for MFJ) is a well-known example of this category.

**3. Tax parity states — deduction available regardless of which state's plan you use.**
As of 2026, approximately nine states offer this: Arizona, Arkansas, Kansas, Maine, Minnesota, Missouri, Montana, Ohio, and Pennsylvania. Residents of these states get to have it both ways — they can shop for the best plan nationally (by fees and investment options) while still claiming their home state's deduction. Deduction caps vary significantly by state (from roughly $1,000 per beneficiary in some states to $19,000+ per beneficiary in others), so confirm the specific state's cap and rules rather than assuming a figure — this list and the specific caps are exactly the kind of state-specific detail that changes with legislation, so verify current rules via a source like savingforcollege.com before relying on it in a client conversation.

**4. States with income tax but no 529 deduction at all.**
A handful of states with an income tax (e.g., California) do not offer any state tax benefit for 529 contributions, in-state plan or otherwise. For these households, the "which plan" decision is purely about fees and investment quality, same as a no-income-tax state — there's no deduction to factor in.

### Practical Guidance
When a client asks about a 529 plan, the actual sequence of questions is: (1) does their state offer a deduction, and is it tied to their own plan or open to any plan (categories 2 vs. 3 above); (2) if tied to their own plan, is that plan actually competitive on fees/investments, or does the deduction not make up for a mediocre plan; (3) if there's no deduction at all (categories 1 or 4), just pick a strong national plan on the merits. Don't default to "use your home state's plan" as boilerplate advice — for households in category 1 or 4, or households in category 2 whose home-state plan is mediocre, that's not actually the right answer.

### Sources
- [529 plans and state tax benefits (J.P. Morgan)](https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/529-documents/529-plan-state-tax-map.pdf)
- [529 Tax Parity States: Full List and Deduction Limits (LegalClarity)](https://legalclarity.org/529-tax-parity-states-full-list-and-deduction-limits/)
- [How Much Is Your State's 529 Plan Tax Deduction Really Worth? (Saving For College)](https://www.savingforcollege.com/article/how-much-is-your-state-s-529-plan-tax-deduction-really-worth)
- [Wyoming 529 Plan Rules And College Savings Options (The College Investor)](https://thecollegeinvestor.com/529-plan-guide/wyoming/)
- [529 contribution limits 2026 (Fidelity)](https://www.fidelity.com/learning-center/smart-money/529-contribution-limits) — annual exclusion, MFJ doubling, superfunding
- [529 Contribution Limits 2026: Maximums by State (Saving For College)](https://www.savingforcollege.com/article/maximum-529-plan-contribution-limits-by-state) — state aggregate balance caps
- [States that do not conform with federal 529 plan tax laws (Saving For College)](https://www.savingforcollege.com/article/states-that-do-not-conform-with-federal-529-plan-tax-laws) — K-12 conformity
- [No Income Tax States 2026 (World Population Review)](https://worldpopulationreview.com/state-rankings/no-income-tax-states)

---

## Trump Accounts (IRC §530A): Custodial Accounts for Minors

### Origin and Core Mechanism
"Trump Accounts" are a new tax-advantaged account for minors, created under **IRC §530A** by the Working Families Tax Cuts title of the One Big Beautiful Bill Act (OBBBA), enacted July 4, 2025. Structurally, a Trump Account functions as **a traditional IRA for a child** during a "growth period" that runs from birth until the year before the beneficiary turns 18 — contributions are non-deductible (after-tax) but grow tax-deferred, and the account is subject to a mandated, narrow investment menu rather than the beneficiary's choice.

**This is new legislation with regulations still being finalized.** IRS Notice 2025-68 (December 2025) gave initial guidance; proposed regulations followed in the Federal Register in March 2026. Treat the mechanics below as current best understanding, not settled final rules — confirm against the latest IRS guidance before relying on specifics in a client conversation, per the skill's Tax Guidance Standard.

### Eligibility and Establishment
- An account may be opened for **any U.S.-citizen child under 18** with a valid Social Security Number, regardless of birth year.
- The election to open an account must be filed **on or before December 31 of the year the child turns 17**, using **IRS Form 4547** (filed with a tax return, submitted separately, or made through the taxpayer's online IRS account).
- **No contributions of any kind may be made before July 4, 2026**, even for accounts established earlier.

### The $1,000 Federal Seed (Pilot Program) Contribution
A one-time **$1,000 federal contribution** is available only for U.S.-citizen children **born January 1, 2025 through December 31, 2028** — this is the "pilot program" cohort, distinct from general eligibility above. It requires an affirmative election on Form 4547 and does **not** count against the $5,000 annual contribution limit. Because it is government money rather than the family's own after-tax contribution, it creates **no basis** — the full $1,000 (plus its growth) is taxable as ordinary income when eventually withdrawn, unlike a personal contribution.

### Annual Contribution Limit ($5,000 Aggregate)
All contributions to a given child's account — from parents, other family, friends, the beneficiary's own earnings, an employer, or a cafeteria plan — **share a single $5,000-per-year cap** (indexed for inflation starting 2027). There is no per-contributor limit within that; the constraint is per child, aggregated across every source. Two sources within that shared cap have distinct tax handling:
- **Individual/family contributions** are non-deductible and establish **basis** — the beneficiary can later withdraw this portion tax-free.
- **Employer contributions**, capped separately at **$2,500/year** (indexed) within the overall $5,000, are deductible to the employer and excluded from the employee's taxable income — but like the federal seed money, they create **no basis** for the beneficiary.

This basis-tracking distinction is the same conceptual trap as the backdoor Roth's pro-rata rule (see above): a withdrawal is taxed based on the *ratio* of contributed-basis to total account value, not on which dollars the family thinks they're pulling out first.

### Investment Requirements During the Growth Period
Unlike a self-directed IRA, funds must be held in a **specific, mandated investment structure** for the entire growth period: an unleveraged mutual fund or ETF tracking a broad index of primarily U.S. companies (an S&P 500-style index is the explicit example in guidance), with **annual fees and expenses capped at 0.10%**. There is no menu choice beyond selecting among funds that meet this test — this is a meaningfully more restrictive structure than a 529 plan's typical age-based or static allocation options.

### Access Restrictions and Conversion to a Traditional IRA at 18
**No distributions are permitted during the growth period** except for a rollover, correction of an excess contribution, or the beneficiary's death — there is **no hardship exception**, which is a stricter rule than either a 529 or a standard IRA. Beginning January 1 of the year the beneficiary turns 18, the account converts to a standard **Traditional IRA**, at which point it can be moved to any custodian, invested at the beneficiary's discretion, and is governed by ordinary Traditional IRA distribution rules going forward (including the 10% early-withdrawal penalty before 59½, subject to the usual IRA exceptions).

### Practical Guidance
- **This is not a 529 substitute.** A 529 offers tax-free growth *and* tax-free qualified withdrawals for education; a Trump Account offers only tax-*deferred* growth, and withdrawals are taxed as ordinary income to the extent they exceed basis, regardless of purpose. For a household focused purely on education funding, the 529 remains the more tax-efficient vehicle — the Trump Account is better framed as a general, restricted-investment head start toward the child's adult financial life (comparable in spirit to a custodial Roth IRA, but funded by others rather than the child's own earned income).
- **Don't assume the $1,000 seed applies broadly.** It's specific to the 2025–2028 birth-year pilot cohort — a family with an older child can still open an account and contribute up to $5,000/year, but will not receive the federal seed money.
- **Flag the basis mechanics before a client contributes.** Because employer and federal-seed dollars carry no basis while personal contributions do, a family funding the account primarily through an employer benefit should understand more of the eventual withdrawal will be taxable than they may assume.
- **Because this is pilot-stage legislation, revisit this section against current IRS guidance before advising on it** — final regulations, contribution mechanics, or the seed-money cohort could still change.

### Sources
- [26 U.S.C. §530A — Trump accounts (U.S. Code, House Office of the Law Revision Counsel)](https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-prelim-title26-section530A&num=0&edition=prelim)
- [IRS Notice 2025-68 — Notice of intent to issue regulations with respect to section 530A](https://www.irs.gov/pub/irs-drop/n-25-68.pdf)
- [Treasury, IRS issue proposed regulations for Trump Accounts contribution pilot program (IRS Newsroom)](https://www.irs.gov/newsroom/treasury-irs-issue-proposed-regulations-for-trump-accounts-contribution-pilot-program-treasury-department-to-deposit-1000-into-the-account-of-each-eligible-child)
- [Treasury, IRS issue proposed regulations on how to open initial Trump Accounts (IRS Newsroom)](https://www.irs.gov/newsroom/treasury-irs-issue-proposed-regulations-on-how-to-open-initial-trump-accounts-under-the-one-big-beautiful-bill)
- [Federal Register: Trump Accounts (proposed rule, March 9, 2026)](https://www.federalregister.gov/documents/2026/03/09/2026-04533/trump-accounts)
- [Form 4547 — Trump Account Election(s) (IRS)](https://www.irs.gov/pub/irs-pdf/f4547.pdf)
- [Instructions for Form 4547 (IRS)](https://www.irs.gov/pub/irs-pdf/i4547.pdf)
- [Trump Accounts: Overview and Policy Considerations (Congressional Research Service, via Congress.gov)](https://www.congress.gov/crs-product/R48910)
- [4 million children have been signed up for Trump Accounts (IRS Newsroom)](https://www.irs.gov/newsroom/4-million-children-have-been-signed-up-for-trump-accounts-with-1-million-claiming-the-1000-pilot-program-contribution)
