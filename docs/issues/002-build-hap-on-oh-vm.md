# Build the HarmonyOS HAP on oh-vm with the native arm64 toolchain

Upstream documents a DevEco Studio (Windows) build. This host builds HarmonyOS packages with the native linux-arm64 Command Line Tools through `oh build`. Until the shell builds here, nothing under `dm/harmony/` can be verified (SOT metric M1).

- **Status:** open (2026-10-26)
- **Severity:** high (blocks every other code issue)
- **Labels:** ready-for-agent
- **Size:** task
- **Context:** W0 of the epic. Needs `local.cmake` (from `local.cmake.example`) and `build-profile.json5` (from the template) — both gitignored, both host-local. `libdm.so` compiles `dm/host` + `dm/gfx/vulkan` + generated headers; some headers are generated from game files (issue 003) — find out which ones block a build without them.

## Items

- [ ] Read skills `vm-openeuler`, `oh-build`; check heavy-job slot before building
- [ ] Create `local.cmake` / `build-profile.json5` on this host (outside git), record what they contain (no secrets) in this issue
- [ ] Determine which generated headers need game files; build without them if possible, else depend on 003
- [ ] Get an unsigned HAP out of `oh build`; record wall-clock and peak RSS
- [ ] Write the exact build line into CLAUDE.md's gate section and `docs/d2r-mobile-architecture.md` §4

## Exit

- [ ] The recorded `oh build` line exits 0 from a clean checkout on oh-vm and produces `entry-default-unsigned.hap` (or signed)
- [ ] `git status` clean afterwards (no generated file or local config tracked)

## Evidence

(none yet)
