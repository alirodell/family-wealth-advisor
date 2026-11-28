# Family Wealth Advisor

A model-agnostic skill for rigorous, direct household financial-planning
analysis — including investment portfolios, retirement planning,
tax-advantaged account strategy, insurance review, and estate planning. It is
packaged for ChatGPT, Codex, Claude Code, and Claude Cowork, but its core
instructions are not tied to a particular model vendor.

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
- Specific call-outs for things people often don't know about or ignore: the backdoor Roth pro-rata trap, why target-date fund vintage should be checked against the money's actual
  horizon rather than the retirement year it's named for (the same check applies to a 529's target-enrollment year), how spousal age
  gaps change Social Security claiming strategy, and why there's nothing to gain from delaying Social Security past 70 (if none of that made sense, don't worry, the drafted plan should explain it).
- **Retirement decumulation guidance** for the years between leaving work and
  claiming Social Security: how to lay out each year's spending, how to compute
  withdrawal taxes with the actual brackets rather than a flat rate (low-income
  years are often taxed far less than people assume), when Roth conversions pay
  and when they don't, and how to size a cash buffer so a bad market early in
  retirement doesn't force you to sell at the bottom. It works from a few numbers
  you can give in conversation; documents make it more precise but aren't required.
- If you provide them, the plan can include a diagnostic on your estate documents, your will, any trusts, etc. I don't actually recommend doing this at first unless you want to go all in. Current language models can be quite good at reviewing these documents against specific life contexts, age, income, and family size. When you combine that output with the financial information this skill helps aggregate, the result can be useful—but it can also get complex quickly.

See [`skills/family-wealth-advisor/SKILL.md`](skills/family-wealth-advisor/SKILL.md)
for the full skill definition and
[`skills/family-wealth-advisor/REFERENCE.md`](skills/family-wealth-advisor/REFERENCE.md)
for cross-cutting reference material (retirement fund mechanics, IRS source
links, etc). See [`CHANGELOG.md`](CHANGELOG.md) for what changed in each version.

## Model-agnostic by design

The core skill uses portable Markdown instructions and reference files. It does
not depend on a particular model name, vendor-specific prompt syntax, or a
single tool implementation. When a capable host provides file access,
calculation tools, and web research, the skill uses those capabilities; when a
tool is unavailable, it falls back to transparent formulas, stated assumptions,
and guidance the user can carry out manually. I have tested the skill across Anthropic and OpenAI models.

## Install

### Codex CLI

Add this repository as a plugin marketplace, then install the plugin:

```sh
codex plugin marketplace add alirodell/family-wealth-advisor
codex plugin add family-wealth-advisor@family-wealth-advisor
```

Start a new Codex session after installation. The skill is discovered
automatically when a request involves household financial planning; no slash
command is required.

### ChatGPT desktop app (local mode)

The desktop app and Codex use the same local plugin marketplace. Add the
repository from a terminal if you have not already done so:

```sh
codex plugin marketplace add alirodell/family-wealth-advisor
```

Then fully quit and reopen the ChatGPT desktop app:

1. Open **Customize** and go to the **Plugins Directory**.
2. Select the `family-wealth-advisor` marketplace.
3. Install **Family Wealth Advisor**.

In a local chat, choose **Family Wealth Advisor** from the composer or mention
it with `@Family Wealth Advisor`. It can also be selected automatically for
relevant financial-planning questions.

### Claude Code

```
/plugin marketplace add alirodell/family-wealth-advisor
/plugin install family-wealth-advisor
```

### Claude Cowork / claude.ai

Open the Customize menu, add this repository
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

None of this is required up front — I recommend starting with a `Client_Profile.md` and a /Investments folder that contains your recent downloaded financial statements. Once you have this then just prompt the skill with `Please run a full wealth diagnostic for me.`. This should generate a 10 section document with recommendations for changes and a score given to each section after about 20 minutes of work. You can absolutely also start with nothing at all, and let it grow over time. If you point the skill at a
directory missing pieces of this structure, it will offer to set them up
rather than assume your data doesn't exist. The inventory files (`investments_inventory.md` and `ss_inventory.md`) let it
cross-check that every account or institution you expect to see is actually
represented, and flag anything missing instead of assuming an account was
closed. If you also save transaction exports (CSV downloads from your 401(k),
brokerage and bank accounts) in `/Investments`, the skill can check how much you
actually saved against what a plan assumes, separating new money from transfers
between your own accounts and from rollovers.

## Testing

The skill's test cases live in
[`skills/family-wealth-advisor/evals/`](skills/family-wealth-advisor/evals/),
one folder per scenario. Each folder holds the prompt a user might type
(`prompt.md`), a plain-language description of a good answer (`case.yaml`), and
one file per check the answer should pass (`graders/`). A case that needs input
files, such as sample transaction exports, keeps them in its own `files/`
folder.

With Claude Code installed, run the whole suite from the skill directory:

```sh
cd skills/family-wealth-advisor
claude plugin eval . --allow-tools Write,Edit,Bash --scaffold
```

`--scaffold` copies each case's input files into place before it runs. The
command runs every case with and without the skill and reports the score for
each. These are real model runs and are billed to your account. To add a
scenario, create a new folder in the same layout.

### Automated checks

GitHub Actions runs free structural checks on every pull request (no model calls):
the plugin manifests agree, the version is bumped when the skill changes and has a
`CHANGELOG.md` entry, every
eval case folder loads correctly, and SKILL.md's structure and internal links are
intact. A weekly job checks the external links in the reference material, and a
reminder opens an issue when the tax figures are a year old and each November when
the next year's thresholds are published. To run the same checks locally:

```sh
pip install pyyaml
python scripts/ci_checks.py all --base origin/main
python scripts/ci_checks.py links
```

## What it doesn't do

This skill provides a more rigorous analysis workflow, not a substitute for a CPA,
CFP, or estate attorney. It's explicitly designed to flag when professional
review is needed before executing rollovers, Roth conversions, insurance
purchases, or estate planning moves — see the skill's "When to Recommend
Professional Review" section.

## A note about the author:
- I have worked in software for almost 30 years. I have also been a bit of a financial planning hobbyist for the same amount of time and happen to have a graduate degree in finance. I realized a few years ago that I had this assumption in my head that "everyone that is good at math must be good at finance"...  It turns out that is not the case, and that not everyone finds learning about finance really interesting... It also turns out that a lot of people's eyes glaze over when you talk about Roth contributions and retirement planning... so I wanted to provide some of my experience in this world to my peers, colleagues and friends so they can educate themselves, open up new avenues for improving their family and personal financial position, and really prepare themselves for having educated conversations with financial and legal professionals.
- Kindly note, I am not a financial advisor, I am not an attorney, I am not a CPA, seriously, this skill is a tool drafted by a financial planning hobbyist to help you think through how best to approach your financial plan for life. If you don't like the output, delete it and hire a professional...

## License

MIT — see [LICENSE](LICENSE).
