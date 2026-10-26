# Make the HarmonyOS build flawless on MateBook Pro S and Mate X5

Umbrella for the huge epic: one HAP, built on oh-vm, that installs, imports, plays and saves flawlessly on the HarmonyOS PC (2in1) and the Mate X5, with touch, keyboard/mouse and gamepad, at 60 fps. Goal, metrics, waves and decisions live in the [SOT](../research/2026-10-26-hmos-flawless/00-epic-sot.md).

- **Status:** open (2026-10-26)
- **Severity:** high (the project's goal)
- **Labels:** ready-for-human
- **Size:** huge epic ([SOT](../research/2026-10-26-hmos-flawless/00-epic-sot.md))
- **Context:** User goal at initialisation, 2026-10-26: "run perfectly on HarmonyOS PC and phones". Upstream verified the shell on Mate 90 Pro Max only (install / import, no performance acceptance) and declares `deviceTypes: ["phone"]`.

## Items

- [ ] Human agrees the SOT metrics M1–M9 (and answers its open questions), then they freeze
- [ ] W0: issues 002, 003, 007, 008
- [ ] W1: issue 004
- [ ] W2: issue 005
- [ ] W3: issue 006
- [ ] W4: performance / stability issues filed from W0–W3 findings
- [ ] E1: human e2e on both devices

## Exit

- [ ] Every SOT exit metric M2–M9 recorded as pass by the human on both devices, with build and firmware
- [ ] All fixes to upstream files offered upstream as PRs (links in the SOT)
- [ ] CHANGELOG entry + version + tag per the huge epic protocol

## Evidence

(none yet)
