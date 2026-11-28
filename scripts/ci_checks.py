#!/usr/bin/env python3
"""Structural checks for the family-wealth-advisor plugin repo.

Run from the repository root:

    python scripts/ci_checks.py manifests [--base REF]   # plugin manifests agree; version bumped vs REF
    python scripts/ci_checks.py evals                    # every eval case folder loads correctly
    python scripts/ci_checks.py skill                    # SKILL.md structure and internal links
    python scripts/ci_checks.py links [--open-issue]     # external links resolve (network)
    python scripts/ci_checks.py freshness [--open-issue] # tax figures are due for re-verification
    python scripts/ci_checks.py all                      # manifests, evals and skill (no network)

Needs Python 3.9+ and PyYAML. Every check prints what it found and exits non-zero on failure,
except freshness, which only reports (and opens a GitHub issue with --open-issue).
"""
import argparse
import concurrent.futures
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

try:
    import yaml                     # needed by the evals and skill checks, not the link check
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "family-wealth-advisor"
EVALS_DIR = SKILL_DIR / "evals"
MANIFESTS = ["plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json"]
MARKETPLACE = ".claude-plugin/marketplace.json"

ALLOWED_SETTINGS = {"tags", "max_turns", "timeout_seconds", "allowed_tools"}
GRADER_TYPES = {"llm", "regex", "file_exists", "tool_used", "tool_order", "baseline"}
RESERVED_CASE_NAMES = {"results", "mocks", "node_modules", "files", "true", "false", "null"}
SKILL_MAX_LINES = 500
DESCRIPTION_MAX_CHARS = 1024
FRESHNESS_MONTHS = 12


class Report:
    """Collects errors for one check and prints a summary."""

    def __init__(self, name):
        self.name, self.errors, self.notes = name, [], []

    def error(self, msg):
        self.errors.append(msg)

    def note(self, msg):
        self.notes.append(msg)

    def finish(self):
        for n in self.notes:
            print(f"  {n}")
        if self.errors:
            print(f"FAIL {self.name}: {len(self.errors)} problem(s)")
            for e in self.errors:
                print(f"  - {e}")
            return False
        print(f"PASS {self.name}")
        return True


def rel(path):
    return str(Path(path).resolve().relative_to(ROOT))


def split_frontmatter(text):
    """Return (frontmatter, body) for a file that starts with a --- block, else (None, text)."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5:]


# ---------------------------------------------------------------- 1. manifests

def check_manifests(base=None):
    r = Report("plugin manifests")
    versions = {}
    for m in MANIFESTS + [MARKETPLACE]:
        p = ROOT / m
        try:
            data = json.loads(p.read_text())
        except FileNotFoundError:
            r.error(f"{m} is missing")
            continue
        except json.JSONDecodeError as e:
            r.error(f"{m} is not valid JSON: {e}")
            continue
        if m == MARKETPLACE:
            names = [pl.get("name") for pl in data.get("plugins", [])]
            if "family-wealth-advisor" not in names:
                r.error(f"{m} does not list the family-wealth-advisor plugin")
            continue
        if data.get("name") != "family-wealth-advisor":
            r.error(f"{m}: name is {data.get('name')!r}, expected 'family-wealth-advisor'")
        v = data.get("version")
        if not isinstance(v, str) or not re.fullmatch(r"\d+\.\d+\.\d+", v):
            r.error(f"{m}: version {v!r} is not MAJOR.MINOR.PATCH")
        versions[m] = v
        if "skills" in data and not (ROOT / data["skills"]).is_dir():
            r.error(f"{m}: skills path {data['skills']!r} does not exist")
    if len(set(versions.values())) > 1:
        r.error("versions differ: " + ", ".join(f"{k}={v}" for k, v in versions.items()))
    current = next(iter(versions.values()), None)
    r.note(f"version {current}")

    changelog = ROOT / "CHANGELOG.md"
    if not changelog.is_file():
        r.error("CHANGELOG.md is missing")
    elif current and not re.search(rf"^## \[?{re.escape(current)}\]?(\s|$)", changelog.read_text(), re.M):
        r.error(f"CHANGELOG.md has no '## {current}' entry; add one describing this version")

    if base and current:
        changed = git("diff", "--name-only", f"{base}...HEAD").split()
        shipped = [f for f in changed if f.startswith("skills/") and "/evals/" not in f]
        try:
            base_version = json.loads(git("show", f"{base}:plugin.json")).get("version")
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            base_version = None
        if shipped and base_version:
            if as_tuple(current) <= as_tuple(base_version):
                r.error(f"skill files changed ({', '.join(shipped[:5])}{'...' if len(shipped) > 5 else ''}) "
                        f"but the version is still {current} (base {base_version}); bump it in all three manifests")
            else:
                r.note(f"version bumped {base_version} -> {current} for skill changes")
        elif not shipped:
            r.note("no shipped skill files changed, so no version bump is required")
    return r.finish()


def as_tuple(v):
    return tuple(int(x) for x in v.split("."))


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True).stdout


# ---------------------------------------------------------------- 2. eval cases

def need_yaml():
    if yaml is None:
        sys.exit("PyYAML is required for this check: pip install pyyaml")


def check_evals():
    need_yaml()
    r = Report("eval cases")
    if (EVALS_DIR / "evals.json").exists():
        r.note("evals/evals.json exists; `claude plugin eval` ignores it, so prefer case folders")
    cases = sorted(p for p in EVALS_DIR.iterdir() if p.is_dir())
    if not cases:
        r.error(f"no case folders under {rel(EVALS_DIR)}")
    for case in cases:
        name = case.name
        where = f"evals/{name}"
        if not re.fullmatch(r"[a-z][a-z0-9-]*", name) or name in RESERVED_CASE_NAMES:
            r.error(f"{where}: invalid case name (lowercase letters, digits, hyphens; not reserved)")

        # prompt.md
        prompt = case / "prompt.md"
        body = ""
        if not prompt.is_file():
            r.error(f"{where}: prompt.md is missing")
        else:
            fm, body = split_frontmatter(prompt.read_text())
            if fm is None:
                r.error(f"{where}/prompt.md: no settings block (--- ... ---) at the top")
            else:
                try:
                    settings = yaml.safe_load(fm) or {}
                except yaml.YAMLError as e:
                    r.error(f"{where}/prompt.md: settings block is not valid YAML: {e}")
                    settings = {}
                unknown = set(settings) - ALLOWED_SETTINGS
                if unknown:
                    r.error(f"{where}/prompt.md: unknown settings {sorted(unknown)} (the case will fail to load)")
            if not body.strip():
                r.error(f"{where}/prompt.md: the prompt is empty")

        # case.yaml
        cy = case / "case.yaml"
        context = {}
        if not cy.is_file():
            r.error(f"{where}: case.yaml is missing")
        else:
            raw = cy.read_text()
            try:
                c = yaml.safe_load(raw) or {}
            except yaml.YAMLError as e:
                r.error(f"{where}/case.yaml: not valid YAML: {e}")
                c = {}
            if c.get("schema_version") != "1.1" or not isinstance(c.get("schema_version"), str):
                r.error(f"{where}/case.yaml: schema_version must be the quoted string \"1.1\"")
            if c.get("name") != name:
                r.error(f"{where}/case.yaml: name is {c.get('name')!r}, expected the folder name")
            if not isinstance(c.get("expected_outcome"), str) or not c["expected_outcome"].strip():
                r.error(f"{where}/case.yaml: expected_outcome is missing or empty")
            context = c.get("context") or {}
            # A literal block (|) keeps line breaks, so a line wrapped right after a hyphen reads
            # back as "word- word". Flag any continuation line that ends in letter+hyphen.
            in_block = False
            for i, line in enumerate(raw.splitlines(), 1):
                if re.match(r"^\w[\w-]*:", line):
                    in_block = line.rstrip().endswith("|")
                    continue
                if in_block and re.search(r"[A-Za-z]-$", line.rstrip()):
                    r.error(f"{where}/case.yaml:{i}: line ends in a hyphen inside a literal block "
                            f"(it will read as 'word- word'); rewrap without breaking on hyphens")

        # graders
        gdir = case / "graders"
        graders = sorted(gdir.glob("*.md")) if gdir.is_dir() else []
        if not graders:
            r.error(f"{where}: no graders/*.md (a case with no grader fails to load)")
        for g in graders:
            gfm, gbody = split_frontmatter(g.read_text())
            gw = f"{where}/graders/{g.name}"
            if gfm is None:
                r.error(f"{gw}: no --- header block (the CLI ignores this file)")
                continue
            try:
                meta = yaml.safe_load(gfm) or {}
            except yaml.YAMLError as e:
                r.error(f"{gw}: header is not valid YAML: {e}")
                continue
            if meta.get("type") not in GRADER_TYPES:
                r.error(f"{gw}: type {meta.get('type')!r} is not one of {sorted(GRADER_TYPES)}")
            if meta.get("type") == "llm" and not gbody.strip():
                r.error(f"{gw}: the statement to grade is empty")

        # input files and scaffold script
        files_dir = case / "files"
        script = context.get("scaffold_script")
        if files_dir.is_dir():
            if not script:
                r.error(f"{where}: has files/ but case.yaml sets no context.scaffold_script")
            m = re.search(r"^Input files:\s*(.+)$", body, re.M)
            if not m:
                r.error(f"{where}/prompt.md: has files/ but the prompt doesn't end with an 'Input files:' line")
            else:
                for f in [x.strip() for x in m.group(1).split(",") if x.strip()]:
                    if not (files_dir / f).is_file():
                        r.error(f"{where}: prompt lists input file {f!r}, which is not in files/")
        if script:
            sp = case / script
            if not sp.is_file():
                r.error(f"{where}: scaffold script {script!r} does not exist")
            elif not os.access(sp, os.X_OK):
                r.error(f"{where}: scaffold script {script!r} is not executable (chmod +x)")
    r.note(f"{len(cases)} case folder(s) checked")
    return r.finish()


# ---------------------------------------------------------------- 3. skill structure + internal links

MD_LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def github_slug(heading, seen):
    """GitHub's heading anchor: lowercase, drop punctuation except - and _, spaces to hyphens."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    s = s.replace(" ", "-")
    n = seen.get(s, 0)
    seen[s] = n + 1
    return s if n == 0 else f"{s}-{n}"


def anchors_of(path):
    seen, out, in_code = {}, set(), False
    for line in path.read_text().splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if m and not in_code:
            text = re.sub(r"`([^`]*)`", r"\1", m.group(2))
            text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
            out.add(github_slug(text, seen))
    return out


def markdown_files():
    skip = {".git", "node_modules"}
    return sorted(p for p in ROOT.rglob("*.md") if not skip & set(p.relative_to(ROOT).parts)
                  and "evals" not in p.relative_to(ROOT).parts)


def check_skill():
    need_yaml()
    r = Report("skill structure and internal links")
    skill_md = SKILL_DIR / "SKILL.md"
    text = skill_md.read_text()
    fm, _ = split_frontmatter(text)
    if fm is None:
        r.error("SKILL.md has no frontmatter block")
    else:
        meta = yaml.safe_load(fm) or {}
        if meta.get("name") != SKILL_DIR.name:
            r.error(f"SKILL.md name is {meta.get('name')!r}, expected {SKILL_DIR.name!r}")
        desc = meta.get("description")
        if not isinstance(desc, str) or not desc.strip():
            r.error("SKILL.md description is missing")
        elif len(desc) > DESCRIPTION_MAX_CHARS:
            r.error(f"SKILL.md description is {len(desc)} characters (limit {DESCRIPTION_MAX_CHARS})")
        else:
            r.note(f"description {len(desc)}/{DESCRIPTION_MAX_CHARS} characters")
    lines = text.count("\n") + 1
    if lines > SKILL_MAX_LINES:
        r.error(f"SKILL.md is {lines} lines (keep under {SKILL_MAX_LINES}; move detail to REFERENCE.md)")
    r.note(f"SKILL.md {lines}/{SKILL_MAX_LINES} lines")

    anchor_cache, checked = {}, 0
    for md in markdown_files():
        body = md.read_text()
        body = re.sub(r"```.*?```", "", body, flags=re.S)       # ignore fenced code
        targets = [m.group(1) for m in MD_LINK.finditer(body)]
        # backticked skill-relative paths such as `references/tier-1-foundational.md`
        if md.is_relative_to(SKILL_DIR):
            targets += [t for t in re.findall(r"`((?:references/[\w.-]+|REFERENCE)\.md)`", body)]
        for t in targets:
            if re.match(r"^[a-z]+:", t):                       # http:, https:, mailto:
                continue
            path_part, _, frag = t.partition("#")
            target = (md.parent / path_part).resolve() if path_part else md
            if not target.is_relative_to(ROOT) or not target.exists():
                # backticked references are relative to the skill directory
                alt = (SKILL_DIR / path_part).resolve() if path_part else None
                if alt and alt.exists():
                    target = alt
                else:
                    r.error(f"{rel(md)}: link target {t!r} does not exist")
                    continue
            checked += 1
            if frag and target.suffix == ".md":
                if target not in anchor_cache:
                    anchor_cache[target] = anchors_of(target)
                if frag.lower() not in anchor_cache[target]:
                    r.error(f"{rel(md)}: anchor '#{frag}' not found in {rel(target)}")
    r.note(f"{checked} internal link(s) checked")
    return r.finish()


# ---------------------------------------------------------------- 5. external links

URL = re.compile(r"https?://[^\s)>\]\"'`]+")
USER_AGENT = "Mozilla/5.0 (compatible; family-wealth-advisor-link-check)"
BLOCKED = {401, 403, 429, 999}     # sites that refuse automated requests; reported, not failed


def probe(url):
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
        if method == "GET":
            req.add_header("Range", "bytes=0-1023")
        for attempt in range(2):
            try:
                with urllib.request.urlopen(req, timeout=25) as resp:
                    resp.read(1024)
                    return "ok", resp.status
            except urllib.error.HTTPError as e:
                if method == "HEAD" and e.code in (400, 403, 404, 405, 429, 501):
                    break                                       # some servers reject HEAD; retry with GET
                if e.code in BLOCKED:
                    return "blocked", e.code
                return "broken", e.code
            except Exception as e:                              # DNS, TLS, timeout
                if attempt == 1:
                    if method == "HEAD":
                        break
                    return "broken", type(e).__name__
    return "broken", "no response"


def check_links(open_issue=False):
    r = Report("external links")
    try:
        import ssl  # noqa: F401  (urllib silently loses https support without it)
    except ImportError as e:
        r.error(f"this Python cannot make HTTPS requests (ssl module unavailable: {e}); use another interpreter")
        return r.finish()
    found = {}
    for md in markdown_files():
        for u in URL.findall(md.read_text()):
            u = u.rstrip(".,;:")
            found.setdefault(u, set()).add(rel(md))
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = dict(zip(found, pool.map(probe, found)))
    broken = {u: s for u, s in results.items() if s[0] == "broken"}
    # If nearly everything failed without an HTTP status, the runner has no network, not dead links.
    no_status = [u for u, (_, code) in broken.items() if not isinstance(code, int)]
    if found and len(no_status) >= 0.9 * len(found):
        r.error(f"{len(no_status)} of {len(found)} URLs failed without any HTTP response; "
                "the network looks unavailable, so no links are being reported as broken")
        return r.finish()
    blocked = {u: s for u, s in results.items() if s[0] == "blocked"}
    r.note(f"{len(found)} unique URL(s): {len(found) - len(broken) - len(blocked)} ok, "
           f"{len(blocked)} refused automated checks, {len(broken)} broken")
    for u, (_, code) in sorted(blocked.items()):
        r.note(f"unverified ({code}): {u}")
    for u, (_, code) in sorted(broken.items()):
        r.error(f"{code}: {u}  (in {', '.join(sorted(found[u]))})")
    ok = r.finish()
    if open_issue and broken:
        body = ["Broken links found by the scheduled link check:", ""]
        body += [f"- `{code}` {u} (in {', '.join(sorted(found[u]))})" for u, (_, code) in sorted(broken.items())]
        body += ["", "Sites that refuse automated checks (403/429) are not listed; check those by hand.",
                 "This issue is updated by each run until the links are fixed."]
        upsert_issue("Broken links in the skill's reference material", "\n".join(body))
    return ok


# ---------------------------------------------------------------- 6. freshness

MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"], 1)}


def check_freshness(open_issue=False, today=None):
    r = Report("tax figure freshness")
    today = today or dt.date.today()
    ref = (SKILL_DIR / "REFERENCE.md").read_text()
    m = re.search(r"Figures last verified:\s*([A-Za-z]+)\s+(\d{4})", ref)
    if not m or m.group(1).lower() not in MONTHS:
        r.error("could not find 'Figures last verified: <Month> <Year>' in REFERENCE.md")
        return r.finish()
    verified = dt.date(int(m.group(2)), MONTHS[m.group(1).lower()], 1)
    age = (today.year - verified.year) * 12 + today.month - verified.month
    r.note(f"figures last verified {verified:%B %Y} ({age} month(s) ago)")
    issues = []
    if age >= FRESHNESS_MONTHS:
        issues.append((
            f"Tax figures in REFERENCE.md (last verified {verified:%B %Y}) are due for re-verification",
            f"REFERENCE.md says its figures were last verified in {verified:%B %Y}, {age} months ago. "
            "Re-check the Current-Year Key Thresholds table against the IRS and SSA sources listed "
            "under it, then update the 'Figures last verified' line."))
    if today.month == 11:
        nxt = today.year + 1
        issues.append((
            f"Update tax thresholds for {nxt}",
            f"The IRS usually publishes the {nxt} inflation adjustments in October or November "
            "(the annual Revenue Procedure), and SSA announces the COLA and wage base in October. "
            f"Update the thresholds table in REFERENCE.md for {nxt} and the 'Figures last verified' line."))
    for title, _ in issues:
        r.note(f"due: {title}")
    if not issues:
        r.note("nothing due")
    if open_issue:
        for title, body in issues:
            upsert_issue(title, body, reopen_closed=False)
    r.finish()
    return True                      # a reminder, never a failure


# ---------------------------------------------------------------- GitHub issues (CI only)

def upsert_issue(title, body, reopen_closed=False):
    """Open an issue with this title, or update the open one. Uses the gh CLI and GH_TOKEN."""
    state = "open" if reopen_closed else "all"
    out = subprocess.run(["gh", "issue", "list", "--state", state, "--search", f'"{title}" in:title',
                          "--json", "number,title,state"], capture_output=True, text=True, check=True).stdout
    match = [i for i in json.loads(out) if i["title"] == title]
    if match:
        if match[0]["state"] == "OPEN":
            subprocess.run(["gh", "issue", "edit", str(match[0]["number"]), "--body", body], check=True)
            print(f"  updated issue #{match[0]['number']}: {title}")
        else:
            print(f"  issue #{match[0]['number']} already exists (closed): {title}")
        return
    subprocess.run(["gh", "issue", "create", "--title", title, "--body", body], check=True)
    print(f"  opened issue: {title}")


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("check", choices=["manifests", "evals", "skill", "links", "freshness", "all"])
    ap.add_argument("--base", help="git ref to compare against for the version-bump rule (e.g. origin/main)")
    ap.add_argument("--open-issue", action="store_true", help="open or update a GitHub issue (CI only)")
    a = ap.parse_args()
    if a.check == "manifests":
        ok = check_manifests(a.base)
    elif a.check == "evals":
        ok = check_evals()
    elif a.check == "skill":
        ok = check_skill()
    elif a.check == "links":
        ok = check_links(a.open_issue)
    elif a.check == "freshness":
        ok = check_freshness(a.open_issue)
    else:
        ok = all([check_manifests(a.base), check_evals(), check_skill()])
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
