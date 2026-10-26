# Install and play the HAP on the HarmonyOS PC (2in1)

The shell declares `deviceTypes: ["phone"]`, so it cannot install on the MateBook Pro S (`2in1`). Add `2in1`, then get the full SOT M2 loop working on the PC: install → import → character select → Rogue camp → save & quit → cold start → continue.

- **Status:** open (2026-10-26)
- **Severity:** high
- **Labels:** ready-for-agent
- **Size:** epic
- **Context:** W1. Code change in upstream's `dm/harmony/` → branch `hmos/004-pc-2in1` from `upstream/main` (ADR-0001). Expect follow-ons: window size / aspect on a 16:10 landscape screen, folder picker behaviour on PC, the form card and backup extension on 2in1, the TLS probe on PC firmware (`dm/harmony/probe/tsd_probe.c`).

## Items

- [ ] Re-run `tsd_probe` on D-PC and confirm the `tpidr_el0 − 272` layout
- [ ] Add `2in1` to `module.json5`; check every API the shell uses is available on 2in1 (skill `harmony-docs`)
- [ ] Sign with our profile for D-PC (skill `harmonyos-atd-provision`), install with `oh app install`
- [ ] Walk the M2 checklist; file each failure as its own issue

## Exit

- [ ] SOT M2 passes on D-PC, recorded with build commit, version code and firmware
- [ ] Same HAP still installs and passes M2 on D-X5 (no phone regression)

## Evidence

(none yet)
