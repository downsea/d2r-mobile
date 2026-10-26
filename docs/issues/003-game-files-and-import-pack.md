# Place the game files and generate a HarmonyOS import pack on this host

Every device test needs the player's own Switch 1.0.34.0 files (`Update/ExeFS/{main,sdk}` + `Update/RomFS/data/`) and an import pack from `d2rm_android.py --target ohos`. Upstream ran that tool on Windows; on Linux arm64 the dependencies (Pillow numpy lz4 capstone unicorn, .NET SDK, spirv-opt with `--trim-capabilities`, spirv-val, glslc, native deswizzle lib) are unverified.

- **Status:** open (2026-10-26)
- **Severity:** high (blocks all device metrics)
- **Labels:** needs-info
- **Size:** task
- **Context:** Needs the user: where the game files are (never in git, never copied into the repo). Disk: pack + data ≈ tens of GB — check the real water level with `disk-guard` first.

## Items

- [ ] User provides the game files' location (outside the repo)
- [ ] `./setup.sh check` on oh-vm; list missing dependencies and how each was satisfied (uv, brew, dnf)
- [ ] Run `d2rm_android.py --target ohos` into a workspace outside the repo; record wall-clock, size, shader count
- [ ] Record the pack's `pack_info.txt` PRODUCT / TARGET

## Exit

- [ ] `<out>/harmony/dm/{out,shaders,overlay,ui-art,derived.tsv,pack_info.txt}` exists and `pack_info.txt` PRODUCT equals `dm/PRODUCT`
- [ ] Nothing under the repo changed (`git status` clean)

## Evidence

(none yet)
