"""Repo-local documentation conventions — the gate's one seam.

`tools/dev/check_docs.py` ships the *family's* mechanical minimum: budget, index, links, tier.
Those hold for every project at this tier. They are not where a repo puts its own rules, and the
observed failure is that a repo-specific convention ("every dataset figure names its convention",
"every rejected option records why") gets checked once by hand when an issue closes, and then rots
— because nothing re-runs it.

This file is that place. It is **repo-owned**: the skill writes it once and never overwrites it.
Fill in `run()` below.

## Contract

    run(root: pathlib.Path, findings: list) -> int | None

- `root` is the repo root.
- `findings` is the gate's own list; append to it. `Finding(kind, severity, path, detail)` is
  injected into this module's namespace, so use it directly.
  - `severity="fail"` → non-zero exit; `"warn"` → reported, green unless `--strict`.
  - `path` should be `"<repo-relative path>:<line>"` so editors can jump to it.
- Also injected, so a rule does not re-derive them:
  - `markdown_files()` → the **same** markdown list the gate scans (already honours
    `SKIP_PATH_PARTS` and `ignore_link_globs`). Use this instead of walking the tree yourself: a
    rule that walks `repos/` reports third-party problems as ours, which is the defect
    `SKIP_PATH_PARTS` exists to prevent.
  - `SKIP_PATH_PARTS` → that set, if you need it directly.
- Return the number of findings added (or `None` to let the gate count them).

Run it alone with `python3 tools/dev/check_docs.py --only conventions`.

## Two rules that make these checks worth having

1. **Measure the trigger's precision before shipping it.** A check that mostly reports noise
   teaches its readers to ignore the whole gate — which costs more than having no check. Write the
   rule, run it over the existing tree, and count how many hits are real. If it is not close to
   100%, narrow the trigger until it is; a rule nobody can satisfy is a rule that gets deleted.
2. **Falsify it, do not just watch it go green.** Inject a violation, confirm the check turns red
   *and* that the process exit code becomes 1, then remove the injection. A check that prints FAIL
   and returns 0 is worse than no check: it will be trusted.

## Where new rules should live

If a rule turns out to hold for **every** project in the family, it does not belong here — move it
upstream into `check_docs.py` so sibling repos get it too. This file is for the rules that are
true of *this* repo, and a growing file here is a signal that the family template is missing
something.
"""

from __future__ import annotations

import os
from pathlib import Path

# `Finding`, `markdown_files` and `SKIP_PATH_PARTS` are injected by check_docs.py before this
# module runs. The fallbacks below keep the file runnable on its own for a quick sanity check
# (`python3 tools/dev/check_conventions.py`) — keep them in sync with the gate's SKIP_PATH_PARTS.
try:
    Finding  # type: ignore[used-before-def]  # noqa: B018
except NameError:  # pragma: no cover

    class Finding:  # type: ignore[no-redef]
        def __init__(self, kind: str, severity: str, path: str, detail: str):
            self.kind, self.severity, self.path, self.detail = kind, severity, path, detail

    SKIP_PATH_PARTS = {".git", "node_modules", "target", ".venv", "__pycache__", "dist", "build",
                       "repos", "data", "runs", "results", ".hf-cache"}

    def markdown_files(root=None):  # type: ignore[misc]
        base = root or Path(__file__).resolve().parents[2]
        out = []
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in SKIP_PATH_PARTS]
            out += [Path(dirpath) / f for f in sorted(filenames) if f.endswith(".md")]
        return sorted(out)

def run(root, findings) -> int:
    """Append this repo's convention violations to `findings`; return how many were added.

    Delete the example below once you have a real rule. It is here so the shape is concrete
    rather than described.
    """
    n = 0

    # --- EXAMPLE (replace me) ------------------------------------------------------------
    # A rule of the form "if a block says X it must also name Y", where the unit is a markdown
    # *block* — a maximal run of non-blank lines: one table row, or one wrapped paragraph. The
    # unit matters: a line-wise rule false-positives on wrapped prose, because the qualifier can
    # land on the previous line.
    #
    # import re
    # figure = re.compile(r"…")
    # qualifier = re.compile(r"…")
    # for path in markdown_files():                     # injected: the gate's own file set
    #     rel = path.relative_to(root).as_posix()
    #     block, start = [], 0
    #     for i, line in enumerate(path.read_text(encoding="utf-8").splitlines() + [""], 1):
    #         if line.strip():
    #             if not block:
    #                 start = i
    #             block.append(line)
    #             continue
    #         if block and any(figure.search(l) for l in block) \
    #                 and not any(qualifier.search(l) for l in block):
    #             findings.append(Finding("example-bare-figure", "fail", f"{rel}:{start}",
    #                                     "figure stated with no qualifier — say which one"))
    #             n += 1
    #         block = []
    # -------------------------------------------------------------------------------------

    return n

if __name__ == "__main__":  # pragma: no cover
    _root = Path(__file__).resolve().parents[2]
    _findings: list = []
    _n = run(_root, _findings)
    for _f in _findings:
        print(f"[{_f.severity.upper()}] {_f.kind}: {_f.path} — {_f.detail}")
    print(f"{_n} finding(s)")
    raise SystemExit(1 if any(f.severity == "fail" for f in _findings) else 0)
