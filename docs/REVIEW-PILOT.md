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

## Results

_(Added after coding.)_
