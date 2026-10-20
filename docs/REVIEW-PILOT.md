# Evidence-first re-review: pilot

_Status: **answer key pre-registered, 20 Oct 2026**, before either coder ran. Results are added below the key; the key is not edited after coding starts._

## Calibration set (24 rows)

Coders see the rows in shuffled order as cases P01–P24, with names, developer, partner, modality, target, indication and source URLs only. "Expected" is the tier the protocol (v0.9) should produce if it works as intended. Ambiguous rows have no expected answer; they test whether two coders agree where the answer is not obvious.

| Row | Current tier | Expected under protocol | Why it is in the set |
|---|---|---|---|
| rentosertib | strict | strict (both) | Clear pass: target and design claims in developer papers |
| dsp-1181 | strict | strict (design) | Clear pass: the first "AI-designed" molecule in the clinic |
| abs-101 | strict | strict (design) | Clear pass: "designed … using our generative AI platform" |
| cly-124 | strict | strict (target) | Clear pass: "AI modeling revealed an undiscovered target" |
| imneskibart | strict | strict (design) | Clear pass: antibody designed by Biolojic's AI platform |
| men2501 | strict | strict (design) | Clear pass: "designed using Insilico's generative AI engine" |
| zovegalisib | borderline | borderline (`physics_only` or `platform_only`) | Known fail (v1.1.18) |
| lirafugratinib | borderline | borderline (`physics_only` or `platform_only`) | Known fail (v1.1.18) |
| migoprotafib | borderline | borderline (`physics_only` or `platform_only`) | Known fail (v1.1.18) |
| rly-5836 | borderline | borderline (`physics_only` or `platform_only`) | Known fail (v1.1.18) |
| sgr-2921 | borderline | borderline (`physics_only`) | Known fail (v1.1.15) |
| ao-252 | borderline | borderline (`platform_only` or `third_party_only`) | Known fail (v1.1.15) |
| ndi-101150 | borderline | borderline (`physics_only`) | Borderline control |
| mrt-2359 | borderline | borderline (`platform_only`) | Borderline control |
| rec-994 | borderline | borderline (`repurposing`) | Borderline control |
| evx-01 | borderline | borderline (`vaccine_antigen`) | Borderline control |
| x-opl-0401 | excluded | excluded (`in_licensed` or `ai_disclaimed`) | Excluded control |
| x-opl-0301 | excluded | excluded (`not_dosed`) | Excluded control |
| x-bmf-219 | excluded | excluded (`no_ai_link`) | Excluded control |
| ac0682 | strict | none (ambiguous) | "AI-enabled platform" with the molecule named, no step |
| env-308 | strict | none (ambiguous) | "discovered using PRISM, Enveda's proprietary AI model" |
| x-ism3312 | excluded | none (ambiguous) | Scope question S3 |
| sgr-1505 | strict | none (ambiguous) | Physics-based FEP+ with a developer ML claim |
| bry10 | strict | none (ambiguous) | Lead optimisation "partly" with an ML engine |

**Success criteria, set in advance:** tier agreement between coders of at least 85% with Cohen's kappa of at least 0.7; at least 18 of the 19 keyed rows reproduced by each coder. Below that, the protocol is revised and the failing rows re-coded before the freeze.

## Results (20 Oct 2026, protocol v0.9)

Two coders, each run as two blind agents (cases P01–P12 and P13–P24), with no access to the registry, its labels or each other. They used 16 web searches in all; the rest was direct fetching. The maintainer session then re-fetched every quoted page: all 95 quotes were found on their pages (90 by script, including Wayback copies of pages that block scripts; 5 read by hand through Firecrawl or a two-column PDF).

| Measure | Result | Pre-set criterion |
|---|---|---|
| Tier agreement, coder A vs B (24 rows) | 23 of 24 (95.8%), Cohen's κ 0.93 | ≥ 85%, κ ≥ 0.7 ✔ |
| Tier and code agreement | 21 of 24 (87.5%), κ 0.84 | none set |
| Keyed rows reproduced, coder A | 18 of 19 | ≥ 18 ✔ |
| Keyed rows reproduced, coder B | 19 of 19 | ≥ 18 ✔ |

| Row | Expected | Coder A | Coder B |
|---|---|---|---|
| rentosertib, dsp-1181, abs-101, cly-124, imneskibart, men2501 | strict | strict (all 6) | strict (all 6) |
| zovegalisib, lirafugratinib, migoprotafib, rly-5836 | borderline | borderline `physics_only` (all 4) | borderline `physics_only` (all 4) |
| sgr-2921, ndi-101150 | borderline `physics_only` | borderline `physics_only` | borderline `physics_only` |
| ao-252 | borderline | borderline `third_party_only` | borderline `platform_only` |
| mrt-2359 | borderline `platform_only` | **strict** (low confidence) | borderline `platform_only` |
| rec-994 | borderline `repurposing` | same | same |
| evx-01 | borderline `vaccine_antigen` | same | same |
| x-opl-0401 | excluded | excluded `ai_disclaimed` | excluded `in_licensed` |
| x-opl-0301 | excluded `not_dosed` | excluded `in_licensed` | excluded `in_licensed` |
| x-bmf-219 | excluded `no_ai_link` | same | same |
| ac0682 (ambiguous) | — | borderline `platform_only` | borderline `platform_only` |
| env-308 (ambiguous) | — | borderline `platform_only` | borderline `platform_only` |
| bry10 (ambiguous) | — | borderline `platform_only` | borderline `platform_only` |
| sgr-1505 (ambiguous) | — | strict (medium) | strict (medium) |
| x-ism3312 (ambiguous) | — | strict (medium) | strict (medium) |

**What the pilot found:**
- **The rules separate the known cases.** All six clear passes stayed strict and all six known fails were caught, each by both coders, without either coder seeing a label.
- **Three current strict rows fail the stricter test,** with both coders agreeing: AC0682 ("program from our AI-enabled drug discovery platform"), ENV-308 ("discovered using PRISM") and BRY10 ("created using MALEXA"). Rows worded like them will fail in the full review too. These are proposals for John, not changes.
- **Two rows pass that the registry does not count as strict today:** ISM3312 (excluded) and SGR-1505 (strict, but questioned as physics-based). Both go to the red team and John.
- **One factual error in the current data:** OPL-0301's exclusion reason says it was never dosed, but Sanofi dosed it in Phase 1 as SAR247799 before Valo in-licensed it. It stays excluded, for a different reason.
- **One rule gap:** "designed using" a multi-method platform (MRT-2359's QuEEN) split the coders. v1.0 closes it (protocol § 9).

**Protocol frozen as v1.0** with the four changes in `REVIEW-PROTOCOL.md` § 9. Under v1.0, MRT-2359 is `platform_only` and AO-252 `platform_only`, matching the key.

## John's blind labels

A 10-row evidence pack, with no labels or verdicts, is in [`REVIEW-PILOT-PACK.md`](REVIEW-PILOT-PACK.md). John's labels will be compared with the coders' here. If they differ in a pattern the protocol does not explain, the protocol goes to v1.1 and the affected rows are re-coded.

_Pending: John's labels._

## After the freeze

The full re-review (158 rows, protocol v1.0, two fresh blind coders) reached tier agreement of 91.8% (κ = 0.87); results are in [`REVIEW-SIGNOFF.md`](REVIEW-SIGNOFF.md) § E. One pilot call changed under v1.0. SGR-1505, passed by both pilot coders, was coded `physics_only` by both full-review coders under the instrument rule. Schrödinger's paper places ML inside "physics-based modeling techniques".

**Protocol v1.1 (20 Oct 2026).** John Milad made the acid test the strict line, and the step test became a flag (`REVIEW-PROTOCOL.md` § 10). The pilot's agreement figures still cover the attribution, dosing and code rules. The 47 platform-level rows were re-coded under v1.1 by two fresh blind coders, who agreed on all 47.
