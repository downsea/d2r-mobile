# Huge epic · HarmonyOS PC + phone, flawless (2026-10-26)

Umbrella issue: [001](../../issues/001-hmos-flawless-on-pc-and-phone.md) ·
Single source of truth: [`00-epic-sot.md`](00-epic-sot.md) (read before touching anything, update after).

## Docs in this epic

| # | Doc | What it holds | Status |
|---|---|---|---|
| 00 | [`00-epic-sot.md`](00-epic-sot.md) | Goal, scope, metrics, waves, decisions, progress | open |
| 01 | (planned) `01-starting-point.md` | W0 findings: what builds / installs / runs on our two devices as of the fork point | not started |
| 02 | (planned) `02-pc-desktop-mode.md` | HarmonyOS 2in1 window modes, key / mouse / pointer APIs, mapping from `dm/host/app_mac.m` | not started |
| 03 | (planned) `03-gamepad.md` | HarmonyOS game controller APIs and the host's pad model | not started |

## Known disagreements between docs

None yet. The orchestrator adjudicates them in the SOT's `## Decisions`, never by editing docs
against each other.

## Inputs (upstream material, read-only)

- [`docs/HARMONYOS.md`](../../HARMONYOS.md) — upstream's player guide; scope of upstream's
  verification on 2026-10-22/23 (Mate 90 Pro Max only; install / import verified, performance
  **not** accepted).
- [`dm/harmony/README.md`](../../../dm/harmony/README.md) — upstream's developer build, HarmonyOS
  defaults table, and the open items (`gfx-present-native`, `NOREDZONE` for ohos).
