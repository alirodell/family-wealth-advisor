# Family Wealth Advisor

A Claude Code / Claude Cowork skill that turns Claude into a rigorous, direct
private wealth advisor for household financial planning — investment
portfolio analysis, retirement planning, tax-advantaged account strategy,
insurance review, and estate planning.

It's not a generic "give me financial advice" prompt. It encodes:

- An **income-tier framework** (five tiers, foundational through legacy/estate
  planning) so the advice given actually matches what's relevant at a
  household's income and net worth — no backdoor Roth guidance for a household
  that isn't phased out of direct Roth contributions yet, no under-serving a
  high earner with beginner-level advice.
- A **10-section Private Wealth Diagnostic** framework for full financial
  reviews (net worth, cash flow, emergency fund, debt, insurance, investment
  allocation, retirement readiness, tax efficiency, estate planning status,
  overall health score).
- Specific, hard-won analytical rules — the backdoor Roth pro-rata trap, why
  target-date fund vintage should be checked against the money's actual
  horizon rather than the retirement year it's named for, how spousal age
  gaps change Social Security claiming strategy, why "we max it out" needs to
  be interrogated rather than taken at face value.

See [`skills/family-wealth-advisor/SKILL.md`](skills/family-wealth-advisor/SKILL.md)
for the full skill definition and
[`skills/family-wealth-advisor/REFERENCE.md`](skills/family-wealth-advisor/REFERENCE.md)
for cross-cutting reference material (backdoor Roth mechanics, IRS source
links).

## Install

**Claude Code:**

```
/plugin marketplace add alirodell/family-wealth-advisor
/plugin install family-wealth-advisor
```

**Claude Cowork / claude.ai:** open the Customize menu, add this repository
as a custom marketplace, then install the `family-wealth-advisor` plugin from
it.

Once installed, the skill triggers automatically on financial-planning
questions — "am I on track for retirement," a full net-worth review, a
backdoor Roth question, a whole life insurance pitch someone's evaluating —
no slash command required.

## What it doesn't do

This skill makes Claude a more rigorous analyst, not a substitute for a CPA,
CFP, or estate attorney. It's explicitly designed to flag when professional
review is needed before executing rollovers, Roth conversions, insurance
purchases, or estate planning moves — see the skill's "When to Recommend
Professional Review" section.

## License

MIT — see [LICENSE](LICENSE).
