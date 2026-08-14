# Family Wealth Advisor

A Claude Code / Claude Cowork skill that turns Claude into a rigorous, direct
private wealth advisor for household financial planning — high level investment
portfolio analysis, retirement planning, tax-advantaged account strategy,
insurance review, and estate planning.

## A note about the author:
- I have worked in software for almost 30 years. I have also been a bit of a financial planning hobbiest for the same amount of time. I realized a few years ago that I had this assumption in my head that "everyone that is good at math must be good at finance"...  It turns out that is not the case, and that not everyone finds learning about finance really interesting... It also turns out that a lot of people's eyes glaze over when you talk about ROTH contributions and retirement planning... so I wanted to provide some of my experience in this world to my peers, colleagues and friends so they can educate themselves, open up new avanues for improving their family and personal financial position, and really prepare themselves for having educated conversations with financial and legal professionals.
- Kindly note, I am not a financial advisor, I am not an attorney, I am not a CPA, seriously, this skill is a tool drafted by a financial planning hobbiest to help you think through how best to approach your financial plan for life. If you don't like the output, delete it and hire a professional...

A few things this skill does. It encodes:

- An **income-tier framework** (five tiers, foundational through legacy/estate
  planning) so the advice given actually matches what's relevant at a
  household's income and net worth — no backdoor Roth guidance for a household
  that isn't phased out of direct Roth contributions yet, no under-serving a
  high earner with beginner-level advice.
- A **10-section Private Wealth Diagnostic** framework for full financial
  reviews (net worth, cash flow, emergency fund, debt, insurance, investment
  allocation, retirement readiness, tax efficiency, estate planning status,
  overall health score). 
- Specific, call outs for things people often don't know about or ignore. - the backdoor Roth pro-rata  trap, why target-date fund vintage should be checked against the money's actual
  horizon rather than the retirement year it's named for, how spousal age
  gaps change Social Security claiming strategy (if none of that made sense, don't worry, the drafted plan should explain it).
- If you provide them, the plan can include a diagnostic on your estate documents, your will, any trusts, etc. I don't actually recommend doing this at first unless you want to go all in. Claude models are actually really quite good at proofreading these documents based on specific life contexts, age, income, family size, etc. When you combine the output of the financial aspects that this skill helps aggregate, the output is really quite interesting and helpful, but...  It can get really complex.

See [`skills/family-wealth-advisor/SKILL.md`](skills/family-wealth-advisor/SKILL.md)
for the full skill definition and
[`skills/family-wealth-advisor/REFERENCE.md`](skills/family-wealth-advisor/REFERENCE.md)
for cross-cutting reference material (retirement fund mechanics, IRS source
links, etc).

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

### Setting up your workspace (optional)

The skill works with no setup at all — just ask it a question. But it works
best when pointed at a working directory holding your actual documents,
since it's built to read source data rather than estimate from memory. A
structure to grow into:

```
your-finances/
├── Client_Profile.md          # ages, income, dependents, mortgage, spending, compensation, etc
├── Financial_Action_Plan.md   # standing action plan + changelog, updated each session
├── Tax_Documents/
│   └── 2026/
├── Investments/
│   └── investments_inventory.md   # institutions you expect statements from
├── Social_Security_Estimates/
│   └── ss_inventory.md            # who should have an SSA estimate on file
├── Prospectuses/               # fund/ETF prospectuses, for allocation lookups
└── Session_Context/            # optional, session-only scratch docs
```

None of this is required up front — I recommend starting with a `Client_Profile.md` and a /Investments folder that contains your recent downloaded financial statements. Once you have this then just prompt the skill with `Please run a full wealth diagnostic for me.`. This should generate a 10 section document with recommendatiosn for changes and a score given to each section after about 20 minutes of work. You can absolutely also start with  nothing at all, and let it grow over time. If you point the skill at a
directory missing pieces of this structure, it will offer to set them up
rather than assume your data doesn't exist. The inventory files (`investments_inventory.md` and `ss_inventory.md`) let it
cross-check that every account or institution you expect to see is actually
represented, and flag anything missing instead of assuming an account was
closed.

## What it doesn't do

This skill makes Claude a more rigorous analyst, not a substitute for a CPA,
CFP, or estate attorney. It's explicitly designed to flag when professional
review is needed before executing rollovers, Roth conversions, insurance
purchases, or estate planning moves — see the skill's "When to Recommend
Professional Review" section.

## License

MIT — see [LICENSE](LICENSE).
