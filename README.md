# AI Molecules in the Clinic

An open registry of drug candidates whose developer credits **AI or machine learning with discovering the target or the molecule**, and which have been **dosed in humans**. Every entry is counted to a written definition, sourced row by row, and open to correction.

**Site:** https://aixbio-registry.org (public from launch day)

**Snapshot:** as of 20 October 2026 · trials retrieved 20 October 2026 · v1.2.0 (proposed, pending sign-off)

| | |
|---|---|
| Strict cohort | **51** molecules |
| Known (precedented) targets, of 46 disclosed | 31 (67.4%) |
| First-in-class targets | 6 |
| Reached Phase 2 or later / now in Phase 3 | 9 / 3 |
| Approved | 0 |
| Stopped (discontinued, terminated, deprioritised) | 10 |
| AI role documented beyond the developer's own word | 1 of 51 |
| Borderline entries (published, not counted) | 66 |

The step-by-step comparison with published counts (Jayatunga 75, Greenblatt & Geoui 83, Haque 117) is in [`METHODOLOGY.md`](METHODOLOGY.md) § 6.

## Why this exists

Counts of "AI-discovered drugs" in the clinic range from about 50 to more than 100 depending on who is counting and what they ask. Most published counts don't release their list or their rules. This one does both, so anyone can check a row, disagree with a call, or recount under a different definition.

## What's here

| File | Contents |
|---|---|
| [`data/molecules.csv`](data/molecules.csv) / `.json` | Strict and borderline entries, one row per molecule, with sources |
| [`data/trials.csv`](data/trials.csv) / `.json` | ClinicalTrials.gov records for the strict cohort (90 trials, 42 molecules) |
| [`data/candidates.csv`](data/candidates.csv) | Possible entries still being checked |
| [`data/excluded.csv`](data/excluded.csv) | Assets considered and excluded, with the reason |
| [`data/audit-log.csv`](data/audit-log.csv) | Evidence for every field of every row: verdict, source URL and a short verbatim quote, dated |
| [`METHODOLOGY.md`](METHODOLOGY.md) | Definition, inclusion tiers, coding rules, known limits |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed in each release |
| [`scripts/`](scripts/) | Build and registry-refresh scripts |

## Corrections

If a row is wrong, missing, or should be reclassified, [open a correction](../../issues/new?template=correction.md) with a source. Corrections are logged in the changelog with the date and the evidence. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Citing

Milad, J. *AI Molecules in the Clinic* (v1.2.0 (proposed, pending sign-off), data as of 20 October 2026). https://github.com/JEM-Fizbit/ai-molecules-in-the-clinic

Data: CC BY 4.0 ([`LICENSE-DATA`](LICENSE-DATA)). Code: MIT ([`LICENSE`](LICENSE)).

## Status and limits, up front

This is independent analysis, not peer-reviewed. Entries were assembled with AI-assisted searches, then re-reviewed against a written evidence protocol by two blind AI coders and a red team, with the maintainer signing off each strict entry. 50 of the 51 strict entries rest on the developer's own statement that AI was used. Read [`METHODOLOGY.md`](METHODOLOGY.md) § Limits before citing.

## Working on the registry

The site is static (`index.html`, `methodology.html`, `assets/site.css`) and reads `data/*.json`. The CSVs are the master: edit them, then run `python3 scripts/csv_to_json.py`. Refresh trials with `scripts/fetch_trials.py`; rebuild the methodology page with `scripts/build_site.py`. Maintainer notes: `CLAUDE.md`, `docs/DECISIONS.md`, `BACKLOG.md`.

