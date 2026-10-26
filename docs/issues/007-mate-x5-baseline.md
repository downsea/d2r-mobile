# Read the Mate X5's facts and get the phone baseline

Our phone is a Mate X5 (foldable), not upstream's Mate 90 Pro Max. The HAP requires API 26; the X5's firmware, API level and GPU are unknown. Connect it, read the facts, install the unchanged shell, and record the SOT M2 / M3 baseline. Then folding (inner / outer screen, unfold mid-game) is a phone-specific stress (SOT M8).

- **Status:** open (2026-10-26)
- **Severity:** high (decides whether the phone target is reachable as-is)
- **Labels:** ready-for-human
- **Size:** task
- **Context:** W0. Device work stays in the main session. If API < 26, the decision (wait for an OTA vs lower `compatibleSdkVersion`) is an ADR, not a drive-by edit.

## Items

- [ ] Connect D-X5 to oh (USB or wireless); record `oh device info` model / software / apiversion / devicetype / abilist into CONTEXT.md and the SOT
- [ ] Re-run `tsd_probe` on D-X5
- [ ] Install the unchanged shell (built by 002), import the pack (003), walk M2
- [ ] Capture an M3 baseline (camp + Den of Evil)

## Exit

- [ ] SOT §2 D-X5 row filled with measured facts
- [ ] SOT M2 / M3 baseline columns filled for D-X5, or a recorded reason why the shell cannot install

## Evidence

(none yet)
