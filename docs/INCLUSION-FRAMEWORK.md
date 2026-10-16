# Inclusion framework — proposal for v2.0

_Status: **proposal v0.1, 16 Oct 2026, for the maintainer's decision.** Once adopted it replaces `METHODOLOGY.md` §1–3. Until then v1.0.0 rules stand._

## Why change v1

v1's definition is sound but too compressed to apply consistently. The data shows the strain:
- **One undifferentiated "material AI role" test.** It treats an AI-nominated target, an AI-generated chemotype and an ML model that tuned an existing series as the same thing. They are not, and readers will want to tell them apart.
- **Borderline is a bin, not a code.** Of 55 borderline entries, 50 carry no machine-readable reason; the reasons are recoverable from free text but fall into eight distinct classes (below).
- **No rule for retrofitted claims**, ie platforms built in the 2010s and rebranded "AI" later, or for narrow uses (one ML property filter among many).
- **No unit-of-analysis rules** for salts, back-ups, combinations, ADCs or personalised vaccines.
- **Single coder.** No inter-rater check on the two judgement calls that matter most: inclusion and target precedence.

## 1. What counts as AI

**Machine learning**: models whose parameters are learned from data — deep learning, generative models (molecules, proteins, antibodies), ML-based QSAR and property prediction, ML virtual screening, knowledge-graph or representation learning, Bayesian optimisation over learned surrogates.

**Not machine learning on its own**: physics-based simulation (docking, free-energy perturbation, molecular dynamics), rule-based expert systems, classical medicinal-chemistry heuristics, and statistical genetics (GWAS, Mendelian randomisation) used without a learned model. These count only where the developer states that an ML component drove the decision in question.

## 2. What the AI did — contribution classes

| Code | Class | Definition | Track |
|---|---|---|---|
| **T** | Target origination | An ML output nominated the target or mechanism the molecule acts on. | Core |
| **M** | Molecule origination | The chemotype or sequence was generated, or selected from a screen, by ML (generative design, ML virtual screening that produced the starting series, ML-based de novo protein/antibody design). | Core |
| **O** | Molecule optimisation | ML predictions drove the design–make–test cycles that produced the clinical candidate from a series that did not originate with ML. | Core |
| R | Repurposing | ML selected a new indication or combination for an existing molecule. | Repurposing track |
| V | Antigen selection | ML selected antigens or epitopes for a vaccine or immunotherapy. | Vaccine track |
| D | Development only | ML used only in patient stratification, biomarkers or trial operations. | Out of scope |

Core entries are labelled **AI-originated** (T and/or M) or **AI-optimised** (O only). A molecule can carry several codes; the label follows the strongest.

**Materiality test.** The contribution must have shaped the target, the chemotype or the identity of the clinical candidate. "ML was used in the programme" is not enough. A single ML filter among many (eg, an hERG predictor used as one gate) fails the test.

**Retrofit rule.** If a platform predates its "AI" branding and no contemporaneous source describes ML use on this molecule, the entry is coded `retrofit` and cannot be Core.

## 3. Evidence of contribution

| Tier | Evidence | Core eligible? |
|---|---|---|
| A | Peer-reviewed paper, regulatory document or patent describing the ML role for **this molecule** | Yes |
| B | Developer's dated public statement specific to **this molecule** | Yes |
| C | Platform-level claim only, or secondary sources only (trackers, press) | No → Watchlist |

## 4. Human-dosing threshold

At least one human dosed, evidenced by a registry record with actual enrolment above zero, or a dated developer or regulatory statement of first dosing. Phase 0 and microdose studies count. Withdrawn studies with no enrolment do not. The as-of date of each entry is recorded.

## 5. Unit of analysis

- One entry per distinct drug substance (INN or lead code). Salts, formulations and routes of the same substance share an entry.
- Back-up or follow-on molecules get their own entry if separately dosed.
- Combinations: one entry per AI-derived component.
- Conjugates and multi-specifics (ADCs, bispecifics, degraders): count if the AI-derived part is the targeting or active moiety; target = the protein bound (degraders: the protein degraded).
- Personalised vaccines: one entry per platform product, not per patient.

## 6. Reason codes for everything outside Core

| Code | Meaning | Where it goes |
|---|---|---|
| `physics-only` | Computational design without an ML claim | Sensitivity track (published, not counted) |
| `platform-only` | Developer claims AI for the platform, not this molecule | Watchlist |
| `secondary-only` | Attribution only from trackers or press | Watchlist |
| `retrofit` | Pre-AI platform rebranded; no contemporaneous ML evidence | Watchlist |
| `non-material` | ML used, but fails the materiality test | Watchlist |
| `repurposing` | Code R | Repurposing track |
| `antigen-selection` | Code V | Vaccine track |
| `development-only` | Code D | Excluded |
| `not-dosed` | No evidence of human dosing | Excluded |
| `ai-disclaimed` | Developer says AI played no part | Excluded |

Every non-Core row must carry exactly one primary code. Watchlist entries are promoted to Core when evidence arrives.

## 7. Coding precedence and status

Unchanged from v1 (`METHODOLOGY.md` §3), with two additions: the precedence date anchor is the molecule's own first-in-human date; for multi-target molecules, code the most precedented intended target and record the others.

## 8. Process and governance

- **Two independent coders** for contribution class, materiality, evidence tier and precedence; disagreements adjudicated and logged; agreement (Cohen's κ) published with each major release.
- **Criteria are versioned.** A change to any definition that can move a molecule in or out of Core is a major version, with a recount and a reconciliation table (what moved, and why).
- **Right of reply.** Developers can contest an entry with evidence through the corrections process; decisions and reasons are public.
- **Conflict-of-interest statement** from the maintainer and any coder, published in the README.

## 9. Decision log and shadow table

The registry records **why** each call was made and keeps every asset it rules out in view, so its own method can be audited and its count reconciled with anyone else's.

**Decision log — `data/decisions.csv` (append-only).** One row per decision: include, exclude, move between tracks, promote from Watchlist, reclassify. Fields: `decision_id`, `date`, `molecule_id`, `from` (track/status), `to`, `reason_code`, `rationale` (one or two sentences), `evidence` (links), `decided_by` (coder initials; adjudicator where coders disagreed), `criteria_version`. Rows are never edited or deleted; a reversal is a new row that cites the one it reverses. Every current row in Core, a track, the Watchlist or the shadow table must trace to at least one decision.

**Shadow table — `data/shadow.csv`.** Every asset that someone else has described as AI-generated, AI-discovered or AI-enabled, but which this registry does not count in Core. Fields: `molecule`, `developer`, `claimed_by` (eg, BCG/Jayatunga 2024; Greenblatt & Geoui 2026; ASCO 2026; developer press; trade trackers), `their_definition`, `our_track` (Watchlist / sensitivity / repurposing / vaccine / excluded), `reason_code`, `decision_id`, `last_reviewed`. Purposes:
- **Not blind to our own method.** Exclusions stay visible and re-reviewable; a criteria change can be re-run over the shadow table rather than re-searched from scratch.
- **Reconciliation with other counts.** A published crosswalk shows, for each external list, how many of its assets are in Core, in a track, on the Watchlist or excluded, and why — turning "why is your number smaller?" into a table.
- **Promotion path.** When evidence arrives, a shadow asset moves to Core through a logged decision.

The current `excluded.csv` (37 rows) and the 55 borderline rows seed both files at v2.0; the external lists are crosswalked where they are published (Jayatunga 2024 supplement; Greenblatt & Geoui on Zenodo). ASCO 2026's 117 cannot be crosswalked until its list is released.

## 10. What adoption would change

- The headline stays one number, the Core count, now split into AI-originated and AI-optimised.
- Repurposing, vaccine and physics-based entries move from "borderline" to named tracks with their own counts.
- Platform-only, secondary-only and retrofit entries become a Watchlist with a stated path to Core.
- Every row gets a contribution code and, if not Core, a reason code, and traces to a logged decision.
- Two new data files: `decisions.csv` and `shadow.csv`, plus a crosswalk against each published external count.
- Work: recode all 109 current entries and the 37 exclusions, seed the decision log, crosswalk Jayatunga and Greenblatt. About a day, plus second coding.
