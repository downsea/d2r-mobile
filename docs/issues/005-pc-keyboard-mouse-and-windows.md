# Keyboard, mouse and window modes on the HarmonyOS PC

The ArkTS shell forwards touch only. On the PC the game must play like the PC game: mouse to move / attack / pick up, keys for skills / belt / map / menus, text entry, and a window that can be windowed, full screen and freely resized (SOT M5, M6). Upstream's macOS app (`dm/host/app_mac.m`) already maps keyboard / mouse onto the host — port its semantics, don't reinvent them.

- **Status:** open (2026-10-26)
- **Severity:** high
- **Labels:** needs-triage
- **Size:** epic
- **Context:** W2. Research first: `docs/research/2026-10-26-hmos-flawless/02-pc-desktop-mode.md` — HarmonyOS key / mouse / pointer events on XComponent, cursor styles, window mode and resize callbacks on 2in1, how the Vulkan swapchain handles resize (`dm/android/vulkan_present.cpp`), touch overlay show / hide policy (design-philosophy P4).

## Items

- [ ] Write research 02 and get it reviewed in the SOT
- [ ] Define the M5 checklist rows (each one action, each one key / mouse gesture)
- [ ] Implement on a `hmos/005-*` branch; touch keeps working on the PC's touch screen

## Exit

- [ ] SOT M5 and M6 checklists pass on D-PC
- [ ] Phone behaviour unchanged (M2 on D-X5 still passes)

## Evidence

(none yet)
