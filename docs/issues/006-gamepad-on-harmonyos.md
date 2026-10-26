# Gamepad support on HarmonyOS (PC and phone)

Upstream supports controllers on iOS / Mac / Android (Xbox and PlayStation layouts). The HarmonyOS shell has no controller input. Make one Bluetooth controller play the full game on both devices without touch (SOT M7).

- **Status:** open (2026-10-26)
- **Severity:** medium
- **Labels:** needs-info
- **Size:** epic
- **Context:** W3. Needs the user: which controller(s) to test with. Research first: `03-gamepad.md` — HarmonyOS game controller / input device APIs and how they map to the host's pad model (`dm/host` padmap, `t_padmap.c`).

## Items

- [ ] User names the controller model
- [ ] Write research 03
- [ ] Implement on a `hmos/006-*` branch; button glyphs follow the controller family

## Exit

- [ ] SOT M7 checklist passes on D-PC and D-X5

## Evidence

(none yet)
