# Generated `UiText.ts` is stale against `ui_text.tsv`, with no gate

Running `dm/harmony/tools/gen_strings.py` on 2026-10-26 at `195ae11` changed `dm/harmony/app/entry/src/main/ets/generated/UiText.ts` (+16/−10 lines: newer import-flow strings such as `dmAndroidImporting`, `dmAndroidImportFailed`, `dmAndroidImportVersion` were missing). The script also writes even when called with `--help`. Nothing checks this file the way `dm_i18n.py --check` checks `dm_i18n_tab.h`.

- **Status:** open (2026-10-26)
- **Severity:** low (wrong / missing shell strings, no crash)
- **Labels:** ready-for-agent
- **Size:** task
- **Context:** Upstream file and upstream bug → fix as an upstream PR (ADR-0001). Note some regenerated strings name Android paths (`Download/S2X/D2R Mobile/`) — check whether the HarmonyOS shell uses those keys before regenerating blindly.

## Items

- [ ] Confirm which `UiText.ts` keys the ArkTS shell uses and whether the Android-path wording is wrong for HarmonyOS
- [ ] Add a `--check` mode to `gen_strings.py` (no write; exit 1 on drift) and make `--help` not write
- [ ] Regenerate `UiText.ts`; open the upstream PR

## Exit

- [ ] `python3 dm/harmony/tools/gen_strings.py --check` exits 0 on the PR branch and 1 when a table row is changed (falsified once)
- [ ] Upstream PR link recorded here

## Evidence

(none yet)
