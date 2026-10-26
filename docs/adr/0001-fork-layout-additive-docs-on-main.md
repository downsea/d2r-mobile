# ADR-0001 · Our doc surface lives on the fork's `main` as additive files; upstream files change only on PR branches

- **Status:** accepted (2026-10-26)
- **Date:** 2026-10-26
- **Scope:** every commit on `downsea/d2r-mobile` `main`; how HarmonyOS code changes travel
- **Decider:** the maintainer (downsea), at project initialisation

## Context

- `downsea/d2r-mobile` is a public fork of `jhaizhou-ops/d2r-mobile`, which commits and merges
  community PRs daily.
- This fork needs a doc surface (`CLAUDE.md`, `docs/`, issues, SOT, a gate) that upstream does not
  have and probably does not want.
- Our goal (HarmonyOS PC + phone) touches upstream's `dm/harmony/` and possibly shared code.

## Decision

We decided **to keep `main` = upstream + additive files only**, and to carry all code changes to
upstream files on branches that become upstream PRs.

Hard lines:

- Files we own on `main`: `CLAUDE.md`, `CONTEXT.md`, `CHANGELOG.md`, `.docs-check.toml`,
  `docs/index.md`, `docs/d2r-mobile-*.md`, `docs/{adr,issues,agents,research}/**`, `tools/dev/**`.
  Nothing else on `main` differs from upstream.
- Syncing upstream is `git fetch upstream && git merge upstream/main` on `main` (no rebase of
  published history).
- A code change goes on a branch cut from `upstream/main` (`hmos/<NNN>-<slug>`), follows upstream's
  CONTRIBUTING, and is offered upstream as a PR. PR branches never contain our doc files.
- Until upstream merges, the build we play is produced from an integration branch
  `hmos/integration` = `upstream/main` + our open PR branches, rebuilt from scratch when either
  side moves. It is never merged into `main`.

## Consequences and costs

- Gained: upstream syncs merge cleanly; every HarmonyOS improvement is upstreamable as-is.
- Paid: our playable build lags `main` by the integration step; PR review latency is upstream's.
- Assumptions to revisit: upstream accepts PC / desktop-input changes in `dm/harmony/`. If a change
  is declined and we still need it, a new ADR decides whether `main` carries a local patch.

## Alternatives

| Option | Why it was not chosen |
|---|---|
| A separate long-lived branch for docs + HarmonyOS work, `main` mirrors upstream | Every agent session would start on the wrong branch; more merge work for no gain |
| Treat the fork as our own project, edit upstream files freely | Gives up on upstream syncs and on contributing back; the user chose to stay downstream |
