# 00 · Epic SOT — HarmonyOS PC + phone, flawless

- **Status:** open (2026-10-26) — chartered; **metrics drafted, not yet agreed or baselined**
- **Umbrella issue:** [001](../../issues/001-hmos-flawless-on-pc-and-phone.md)
- **Fork point:** upstream `195ae11` (2026-10-24), `dm/PRODUCT` = `3.3.94012-r44`

## 1. Goal

One HAP, built on oh-vm, that a player installs over the top on a **HUAWEI MateBook Pro S**
(`2in1`) and a **HUAWEI Mate X5**, imports their own game files into, and plays from new game to
endgame: 60 fps, keyboard + mouse and windowed play on the PC, touch on both, a gamepad on both,
and no lost save through upgrades, lifecycle events, folding, long sessions and backup / restore.

Acceptance scope chosen by the user (2026-10-26): PC installs and plays · PC keyboard / mouse and
windows · phone performance acceptance · phone long-run stability · gamepad support.

## 2. Devices

| Id | Device | Facts | Source |
|---|---|---|---|
| D-PC | HUAWEI MateBook Pro S, `MOR-M1` | `2in1`, OpenHarmony-7.0.0.109, `MOR-W52 7.0.0.111`, API 26, arm64-v8a | `(measured 2026-10-26, oh device info)` |
| D-X5 | HUAWEI Mate X5 | firmware / API / GPU **unknown** — HAP requires API 26 | to read in W0 (issue 007) |

## 3. Metrics (DRAFT — to be agreed with the human, then baselined in W0, then frozen)

Wave metrics (W) are scored by the orchestrator; exit metrics (E) only by the human on the device.

| Id | Kind | What | Exact command / procedure | Baseline (now) | Target | Judge |
|---|---|---|---|---|---|---|
| M1 | W | HAP builds on oh-vm from a clean tree | `oh build` line from issue 002; exit 0 and HAP present | not measured | pass | orchestrator |
| M2 | E | Full loop per device: install over the top → import → character select → enter Rogue camp → save & quit → cold start → continue | Checklist in issue 004 (PC) / 007 (X5), `oh app install` + manual play | D-PC: cannot install (`deviceTypes` = phone); D-X5: unknown | pass on both | human |
| M3 | E | Frame pacing in play | `oh perf` / hitrace capture, 60 s in Rogue camp + 60 s fighting in Den of Evil; present interval p50 / p99 | not measured | p50 ≤ 16.8 ms, p99 ≤ 20 ms on both devices | human (numbers from orchestrator) |
| M4 | E | Long session | 60 min continuous play per device; crashes, p50 fps in the last 10 min, save files intact | not measured | 0 crashes, p50 ≥ 58 fps, saves byte-identical after save & quit | human |
| M5 | E | PC keyboard + mouse | Checklist (issue 005): move / attack / skills on keys / inventory drag / belt / map / menus / text entry — all **without touching the screen** | not possible (touch only) | every checklist row passes | human |
| M6 | E | PC windowing | Windowed ↔ full screen, free resize 10 cycles, minimise / restore; correct aspect, no stretched UI, no crash | not measured | pass | human |
| M7 | E | Gamepad | One Bluetooth controller, both devices: full checklist (issue 006) without touch | not possible | pass on both | human |
| M8 | E | Lifecycle | 10× background / foreground, 10× fold / unfold (X5), PC sleep / resume, while in game | not measured | 0 crashes, no black screen, saves intact | human |
| M9 | E | Save safety | Upgrade over the top + system backup / restore; hash saves before / after (`oh app` sandbox read) | not measured | hashes equal | human |

Open questions for the human before freezing: the gamepad model to test with; whether M3's target
is per-device-native refresh or a fixed 60 Hz; the save-file hashing method.

## 4. Waves (plan)

| Wave | Content | Issues | Batch / agents |
|---|---|---|---|
| W0 | Baseline: toolchain build (M1), game files + import pack, read D-X5 facts, phone-only HAP onto D-X5, measure M2/M3 baselines | 002, 003, 007, 008 | main session (device work) |
| W1 | PC: `2in1` device type, install + boot + import + play on D-PC | 004 | ≤ 1 writable agent |
| W2 | PC desktop mode: keyboard / mouse / windowing (research 02 first) | 005 | ≤ 2 (research ‖ implementation of independent parts) |
| W3 | Gamepad on both (research 03 first) | 006 | ≤ 2 |
| W4 | Performance + stability on both: M3, M4, M8, M9 | new issues from W0–W3 findings | — |
| E1 | Human e2e on both devices | — | human |

## 5. Decisions

| Date | Decision | Why |
|---|---|---|
| 2026-10-26 | Docs on fork `main`, code via upstream-PR branches + `hmos/integration` build branch | [ADR-0001](../../adr/0001-fork-layout-additive-docs-on-main.md) |
| 2026-10-26 | Tier 2; target devices = D-PC + D-X5 only | User at initialisation |

## 6. Progress

| Date | Wave | What happened | Metrics | Commits |
|---|---|---|---|---|
| 2026-10-26 | — | Epic chartered; doc surface initialised | none measured | (initialisation commit) |
