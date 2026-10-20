# Changelog

## v1.1.1 — 2026-10-20
Open checks from the 13 October build, closed against sources. No change to any inclusion call. Strict status moves from 36 ongoing / 15 stopped / 3 unknown to 38 / 15 / 1.
- DSP-0038 and DSP-2342: `unknown` → `ongoing`. Both are listed at Phase 1 in Sumitomo Pharma's development pipeline as of 31 July 2026 (Q1 FY2026 materials). NCT07850102, a Johns Hopkins imaging study of DSP-2342, is not yet recruiting.
- MEN2312 is Insilico's ISM5043, per Menarini (10 January 2025) and Insilico's KAT6 program page; the "code mapping provisional" label is removed.
- ISM3091 / XL309: still in Phase 1 with enrollment ongoing, per the Exelixis 10-Q filed 5 August 2026.
- RTX-117: first participant dosed in a China healthy-volunteer Phase 1, announced by ReviR on 2 March 2026; first-in-human year corrected from 2025 to 2026. Registry IDs added: CTR20255232, ChiCTR2600118758.
- SIGX1094: China registry ID CTR20243995 added (first enrollment 26 December 2024).
- ENV-294: Phase 2b confirmed by the title of NCT07643766. The two Phase 2a trials, NCT07298395 (atopic dermatitis) and NCT07301255 (asthma), are added.
- iscartrelvir: approval date set to 29 July 2026 (conditional, China NMPA). Sources added: the 2023 paper (ACS Central Science), Westlake Laboratory's account of the discovery (September 2026) and Westlake Pharmaceuticals' product page. Its inclusion stays borderline pending review.
- Two internal process notes removed from `notes`.

## v1.1.0 — 2026-10-20
Corrections without a GitHub account; no change to any count, inclusion or coding call.
- Correction form on the site (no account needed), with bot traps and a per-connection hourly limit. Submissions go to a private database; the submitter's name and email are never published.
- Public corrections log on the site, listing decided corrections with outcome and reason.
- Each entry's detail view links to the form, prefilled with that molecule.
- Maintainer review page (`admin.html`, password-protected) and a small API (`api/`), running in London.

## v1.0.1 — 2026-10-19
Site and housekeeping; no change to any count, inclusion or coding call.
- New public site: the census of all 54 strict molecules by furthest phase, the comparison with other published counts, a searchable registry with per-molecule detail, and the methodology rendered as its own page (`methodology.html`, built by `scripts/build_site.py`).
- Site, after review: a key explaining the four target types; first-in-class shown in gold (red is kept for stopped programmes); census stacks fill from the bottom so the partial row sits on top; registry table gains a modality class (small molecule, antibody, peptide, vaccine, other biologic) and a "next data due" column, the estimated primary completion of the soonest active ClinicalTrials.gov trial.
- `notes`: removed an internal build marker ("NEW vs 37", a reference to an unpublished earlier reconstruction) from 27 rows; kept the registry-only facts it carried for two rows (ANZCTR, jRCT).

## v1.0.0 — 2026-10-16
First public release. Data as of 13 October 2026; ClinicalTrials.gov trials retrieved 15 October 2026.
- 54 strict, 55 borderline, 7 candidates, 37 excluded; 80 ClinicalTrials.gov trials for 47 strict molecules.
- Supersedes an unpublished 37-molecule reconstruction (August 2026) that searched ClinicalTrials.gov only. The rebuild added non-US registries, out-licensed assets and biologics (27 added, 10 dropped).
