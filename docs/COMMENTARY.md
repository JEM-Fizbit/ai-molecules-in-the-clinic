# Commentary register

Every statement about the registry's numbers, on the site or elsewhere, must still be true after each data release. This file lists how each one is kept true. **Read it at every release**, after `check_counts.py` passes. The CHANGELOG entry ends with a "Commentary reviewed" line that names anything changed, or says nothing needed changing.

## 1. Computed: updates itself

The site computes these in the browser from `data/*.json` on every page load. No action is needed.

- Home page hero: the strict count; approvals; known targets of disclosed; novel targets with percentage and split; randomized readouts on novel targets; tier-A attribution; Phase 2 outcomes. The qualitative words switch with the data too: "Most / Half / Fewer than half" known, "None is / One is / N are approved", and "too few / enough to compare" (the switch is at 10 outcomes, as on the question page).
- Census chart, registry table, limits list, "Why other counts are bigger" (this registry's bar only).
- Question page: the forest plot, its bars and its labels.

## 2. Checked: the QA gate fails if it drifts

`scripts/check_counts.py` compares the following text with the data:

- Numbers written into README.md and METHODOLOGY.md.
- The fallback text the site shows before its script runs and in link previews (`og:description`).
- The **readout watch**. A Phase 2+ trial of a novel-target molecule whose primary completion date has passed must have a row in `data/readouts.csv`: either the readout, or `randomized_efficacy = no` with the date it was checked. A "no" row expires after 180 days. This keeps "one has a randomized readout" from going stale silently.

## 3. Manual: review at each release

| Statement | Where | Goes stale when |
|---|---|---|
| Other published counts (Jayatunga, Greenblatt & Geoui, Haque and others) and their notes | `index.html` `OTHER` array and references; METHODOLOGY § 6 | An author publishes an update, or our reading of their scope changes |
| Industry benchmarks (BIO, DiMasi, Wong, Hay) and "about 1 in 13", "fewer than 3 in 10" | `question.html` | A new benchmark study is added |
| "Other counts reach other answers" (Jayatunga's ~40% Phase 2) | `question.html` limits | Jayatunga or successors update |
| The re-review notice | `index.html` limits; METHODOLOGY § 7 | The re-review completes (remove or rewrite it) |
| Uncertainty band prose and row lists | METHODOLOGY § 5 | Any inclusion change touching physics or platform entries (the band figure itself is checked) |
| Readout coverage: "complete for novel targets; known targets not yet recorded" | METHODOLOGY § 4 | Coverage is extended, or a novel-target molecule is added |
| Pre-release notice ("not yet formally released as v1 … don't cite the figures yet") | `index.html` hero and `og:description`; README | The formal v1 release: remove it then |
| "Why this exists" | README.md | The registry's purpose or scope changes |

## 4. Outside the repo: the essay and the talk

These figures were published or spoken before the registry's October 2026 corrections. When a release moves any of them, say so in the CHANGELOG entry and tell the essay workspace.

| Claim as made | Current registry (v1.1.23) | Status |
|---|---|---|
| Fifty-four AI-derived molecules dosed in people | 49 | Update |
| Three in four on known targets | 33 of 47 disclosed (70%), about seven in ten | Update |
| None approved | None | Holds |
| Phase II success about 40%, the same as history | The ~40% is Jayatunga 2024's figure, not the registry's. Only 5 registry molecules have a Phase 2 outcome. Published industry Phase 2 rates are about 29–58% (median about 32%). | Drop, or attribute to Jayatunga |
| Of the fourteen on novel targets, one (rentosertib) has a randomized efficacy readout | 14 of 47 (30%); one, rentosertib (Phase 2a, efficacy a secondary endpoint) | Holds; say "randomized, placebo-controlled readout with efficacy data" |
