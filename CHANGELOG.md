# Changelog

What changed in each version of the Family Wealth Advisor plugin. The version is
the one in the plugin manifests (`plugin.json`, `.claude-plugin/plugin.json`,
`.codex-plugin/plugin.json`): a **minor** version adds or changes guidance, and a
**patch** version updates figures or fixes errors without changing how the skill
works. Changes to the repository itself (CI, README) are listed under the next
release, or under **Unreleased** until one ships.

## Unreleased

### Repository
- Added this changelog, linked from the README, and a CI check that fails if the
  plugin's version has no entry here.

## 1.4.1 — 2026-11-28

### Changed
- Tax thresholds updated for 2027: the table in `REFERENCE.md` shows 2026 and 2027
  side by side during the changeover. Sources: Rev. Proc. 2026-35, Notice 2026-66
  and Rev. Proc. 2026-24.
- The Saver's Credit is replaced by the **Saver's Match** for retirement
  contributions from 2027: a federal deposit of 50% of up to $2,000 a year into the
  saver's retirement account, with lower income limits. The Tier 1 playbook is
  updated to match.
- The mega-backdoor Roth, estate and 529 sections now cite 2027 figures.

### Repository
- Added GitHub Actions: structural checks on every pull request (manifests, eval
  cases, `SKILL.md` structure and internal links), a weekly external-link check,
  and a tax-figure freshness reminder that opens an issue.
- README: described the 1.4.0 guidance, added a Testing section, fixed typos.

## 1.4.0 — 2026-11-28

### Added
- Retirement decumulation guidance for the years between leaving work and
  claiming Social Security: a year-by-year bridge layout, bracket-based withdrawal
  taxes in low-income years (instead of a flat rate), Roth conversion economics,
  cash buffers going into retirement, and savings-rate inputs. Each works from a
  few numbers given in conversation; documents sharpen the inputs.
- The target-date vintage check now covers 529 target-enrollment portfolios.
- A rule to say which figures changed when revising an earlier model.
- `REFERENCE.md`: 2026 long-term capital gains bands, RMD starting ages by birth
  year, and a Retirement Decumulation section (break-even method, tax stacking
  steps, conversion cost, cash-buffer arithmetic).
- Five eval cases: bridge withdrawal taxes, a Roth conversion paid from
  appreciated holdings, claiming at 70½, savings from transaction exports, and a
  sparse-data bridge question.

### Changed
- Evals moved from `evals/evals.json` to one folder per case, the layout
  `claude plugin eval` runs. `evals.json` was removed.

## 1.3.0 — 2026-10-31

### Added
- `REFERENCE.md`: a Retirement Income section (Social Security, Medicare and
  IRMAA, the pre-Medicare healthcare bridge) and an Equity Compensation and
  Investment Protections section.
- Primary sources for existing sections (IRS notices and publications, Form 709,
  estate and gift tax pages).

### Fixed
- Dead reference links (statute links, a retired article, an outdated Form 8606
  PDF).

## 1.2.0 — 2026-09-26

### Changed
- Made the skill model-agnostic: vendor-neutral instructions, a fallback to shown
  formulas when no calculation tool is available, and a proposed action-plan entry
  when no writable workspace is available.
- Packaged for Codex and the ChatGPT desktop app as well as Claude Code and
  Cowork (Codex plugin manifest, icon and logo), with install instructions for each.

## 1.1.0 — 2026-08-09

### Added
- Trump Accounts (IRC §530A) reference section: eligibility, the $1,000 seed
  contribution, the $5,000 shared annual cap and its basis tracking, investment
  rules, and conversion to a traditional IRA at 18.
- A recommended household workspace structure (client profile, action plan,
  document inventories) and a session workflow that reads source documents rather
  than estimating from memory.

## 1.0.0 — 2026-08-08

### Added
- First release as a standalone plugin: the income-tier framework (five tiers),
  the 10-section Private Wealth Diagnostic, cross-cutting reference material
  (backdoor Roth and the pro-rata rule, mega-backdoor Roth, whole life insurance
  mechanics, estate tax exemptions, 529 plans), and the first evals.
