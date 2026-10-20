# AI Molecules in the Clinic

An open registry of drug candidates whose **target or molecule was materially shaped by AI or machine learning** and which have been **dosed in humans**. Every entry is counted to a written definition, sourced row by row, and open to correction.

**Site:** https://aixbio-registry.org (public from launch day)

**Snapshot:** as of 20 October 2026 · trials retrieved 20 October 2026 · v1.1.14

| | |
|---|---|
| Strict cohort | **55** molecules |
| Known (precedented) targets, of 51 disclosed | 37 (72.5%) |
| First-in-class targets | 5 |
| Reached Phase 2 or later / now in Phase 3 | 12 / 4 |
| Approved | 1 (lirafugratinib, FDA, 23 September 2026) |
| Stopped (discontinued, terminated, deprioritised) | 15 |
| AI role documented beyond the developer's own word | 1 of 55 |
| Borderline entries (published, not counted) | 60 |

## Why this exists

Counts of "AI-discovered drugs" in the clinic range from about 50 to more than 100 depending on who is counting and what they ask. Most published counts don't release their list or their rules. This one does both, so anyone can check a row, disagree with a call, or recount under a different definition.

## What's here

| File | Contents |
|---|---|
| [`data/molecules.csv`](data/molecules.csv) / `.json` | Strict and borderline entries, one row per molecule, with sources |
| [`data/trials.csv`](data/trials.csv) / `.json` | ClinicalTrials.gov records for the strict cohort (83 trials, 47 molecules) |
| [`data/candidates.csv`](data/candidates.csv) | Possible entries still being checked |
| [`data/excluded.csv`](data/excluded.csv) | Assets considered and excluded, with the reason |
| [`data/audit-log.csv`](data/audit-log.csv) | Evidence for every field of every row: verdict, source URL and a short verbatim quote, dated |
| [`METHODOLOGY.md`](METHODOLOGY.md) | Definition, inclusion tiers, coding rules, known limits |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed in each release |
| [`scripts/`](scripts/) | Build and registry-refresh scripts |

## Corrections

If a row is wrong, missing, or should be reclassified, [open a correction](../../issues/new?template=correction.md) with a source. Corrections are logged in the changelog with the date and the evidence. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Citing

Milad, J. *AI Molecules in the Clinic* (v1.1.14, data as of 20 October 2026). https://github.com/JEM-Fizbit/ai-molecules-in-the-clinic

Data: CC BY 4.0 ([`LICENSE-DATA`](LICENSE-DATA)). Code: MIT ([`LICENSE`](LICENSE)).

## Status and limits, up front

This is independent analysis, not peer-reviewed, and not yet second-coded by an independent human reviewer. Entries were assembled with AI-assisted searches and checked by an adversarial verification pass. 54 of the 55 strict entries rest on the developer's own statement that AI was used. Read [`METHODOLOGY.md`](METHODOLOGY.md) § Limits before citing.

## Working on the registry

The site is static (`index.html`, `methodology.html`, `assets/site.css`) and reads `data/*.json`. The CSVs are the master: edit them, then run `python3 scripts/csv_to_json.py`. Refresh trials with `scripts/fetch_trials.py`; rebuild the methodology page with `scripts/build_site.py`. Maintainer notes: `CLAUDE.md`, `docs/DECISIONS.md`, `BACKLOG.md`.

