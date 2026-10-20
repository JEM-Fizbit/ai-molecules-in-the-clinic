# Methodology

Version 1.2.0 (proposed, pending sign-off) · data as of 20 October 2026

## 1. Definition

A molecule is in the **strict cohort** if all three hold:

1. **Material AI/ML role** in choosing the target or designing the molecule. Machine learning or generative methods did real work in target identification or molecule design, not only in screening logistics or general analytics.
2. **Attribution.** The developer or a partner states, in its own words, that AI or ML did that work for *this* molecule, and says what it did: chose the target, or designed the molecule. Platform-level language ("developed using our AI platform", "discovered with our AI-enabled engine") is not enough. Third-party statements are not enough.
3. **Dosed in humans** by the as-of date, by any sponsor, in any registry (ClinicalTrials.gov, ANZCTR, jRCT, China CTR or equivalent) or per a dated developer statement.

The tests are applied by the written evidence protocol in [`docs/REVIEW-PROTOCOL.md`](docs/REVIEW-PROTOCOL.md): two blind coders per row, a red team arguing for exclusion on every strict pass, and the maintainer's sign-off on every strict entry. The acid test: if the developer does not claim the molecule as AI-derived in its own words, neither does the registry.

## 2. Inclusion tiers

| Tier | Meaning | Counted? |
|---|---|---|
| `strict` | Meets all three tests | Yes |
| `borderline` | Dosed, with an AI connection, but not strict. One code in `borderline_reason`: `physics_only` (computational design with no ML claim for this molecule), `platform_only` (the developer ties the molecule to an AI platform but never says what the AI did), `third_party_only`, `repurposing` (AI picked a new use for an existing drug), `vaccine_antigen` (AI-selected antigens) or `other` | No, but published with the reason in `inclusion_note` |
| `candidate` | Plausible but not yet verified | No |
| excluded | Considered and rejected; one code in `exclusion_code`: `not_dosed`, `ai_disclaimed`, `in_licensed`, `legacy_retrofit`, `out_of_scope` or `no_ai_link` | No; listed in `excluded.csv` |

## 3. Coding rules

- **Target precedence** (`target_precedence`), judged at the molecule's first-in-human date:
  - `precedented` (shown on the site as "Known target"): an approved drug or a Phase 2+ agent already existed at the target.
  - `novel`: clinical agents existed at the target, but none at Phase 2+.
  - `first-in-class`: no prior clinical agent at the target.
  - `unclear`: target undisclosed or not determinable.
  The basis for each call is in `precedence_basis`.
- **Attribution tier** (`attribution_tier`): `A` = peer-reviewed or regulatory documentation of the AI role; `B` = developer disclosure; `C` = secondary sources only (C-only entries go to borderline).
- **Status** (`status`): `ongoing`; `stopped` (discontinued, terminated, completed with no further development, or deprioritised); `unknown` (no update for over 18 months and no discontinuation notice). Detail in `status_detail`.
- **Confidence** (`confidence`): the coder's confidence in the row as a whole.
- **AI-claim evidence** (`ai_claim_quote`, `ai_claim_url`, `ai_claim_by`, `ai_claim_date`, `ai_step`): the single best verbatim claim (40 words or fewer) that AI or ML did work for this molecule, where it was published, who made it (`developer`, `partner`, `developer_paper` or `third_party`), when, and the step it names (`target`, `design` or `both`; blank if it names none). Rules for choosing and testing it are in `docs/REVIEW-PROTOCOL.md`.
- **Borderline reason** (`borderline_reason`): one code per borderline row: `physics_only`, `platform_only`, `third_party_only`, `repurposing`, `vaccine_antigen` or `other`. Excluded rows carry an `exclusion_code` in `excluded.csv`.

## 4. How the list was built

Six parallel searches: published seed lists (BCG/Jayatunga 2024 and successors); AI-native small-molecule developers in the US, Europe and Israel; Asia-Pacific developers and registries; biologics; pharma-internal assets; and an asset-agnostic registry and literature sweep. Results were merged and coded, then challenged by two independent passes: one trying to disprove entries (about 50 registry records re-checked) and one looking for missing assets. Searches were AI-assisted; every row carries its sources. In October 2026 every stopped, unknown and Phase 2+ status was re-checked against its registry and every source link was verified (v1.1.2 and v1.1.3 in `CHANGELOG.md`).

**Evidence-first re-review (October 2026).** Every row, strict, borderline and excluded, was re-coded under the protocol in `docs/REVIEW-PROTOCOL.md` by two coders who could not see the current tiers or each other's work. The protocol was piloted first on 24 rows with known answers (`docs/REVIEW-PILOT.md`; coder agreement κ = 0.93). On all 158 rows the coders agreed on the tier for 145 (91.8%, κ = 0.87). A red team then argued for exclusion on all 38 rows that either coder passed as strict, and defeated 6. Every quoted claim was re-fetched and found on its page. The registry was also cross-checked against four published lists (`data/crosswalk.csv`).

Trials (`trials.csv`) are every ClinicalTrials.gov record matched to a strict-cohort molecule by NCT number or verified intervention name (API v2, retrieved 20 October 2026). Five strict molecules have no ClinicalTrials.gov record. Posted protocols and statistical analysis plans are linked where the sponsor has uploaded them.

Approvals (`approvals` in `molecules.csv`) record each regulatory approval as agency, date, application or approval reference, indication and a link to the regulator's own record (Drugs@FDA for US approvals). A molecule can be approved and still `ongoing` when trials in other indications continue.

## 5. Uncertainty

The strict count is about **32, −2/+8**:
- dosing and attribution errors: about ±2. Four strict entries (DSP-1181, DSP-2342, EXS-4318, ISM3312) rest on developer statements of dosing with no registry record read, and the maintainer's sign-off may still move contested entries (`docs/REVIEW-SIGNOFF.md`);
- assets probably missing, mainly from China CTR and recent US first-in-human starts: +0 to +6;
- definition sensitivity, each computed from `borderline_reason` in `molecules.csv`:
  - counting physics-based design gives **50**: adding the 18 borderline `physics_only` entries;
  - counting platform-level attribution gives **71**: adding the 39 borderline `platform_only` entries.

The ±2 and +0 to +6 components are judgement, not computed; the +0 to +6 comes from the completeness pass of the 13 October 2026 build.

## 6. Other counts, and why they differ

| Count | Number | Definition |
|---|---|---|
| [Jayatunga et al. 2024 (BCG)](https://doi.org/10.1016/j.drudis.2024.104009), *Drug Discovery Today* | 75 | Clinical assets of AI-native companies since 2015 |
| [Greenblatt & Geoui 2026](https://doi.org/10.5281/zenodo.22814924) (Zenodo) | 83 | BCG list plus additions |
| [McKinsey 2026](https://www.mckinsey.com/industries/life-sciences/our-insights/ai-drug-discovery-focusing-on-what-matters-most), Exhibit 2 | 9 | Examples of "AI-enabled assets" with disclosed cycle times; non-exhaustive |
| [Haque et al., ASCO 2026](https://doi.org/10.1200/JCO.2026.44.16_suppl.11072) | 117 | "AI-enabled"; list not published |
| This registry | 32 | Molecule-level attribution, dosed in humans, written rules |

Lower is not more correct. Each count answers a different question; this one asks the narrowest. `data/crosswalk.csv` maps every entry of the Jayatunga, Greenblatt & Geoui, Wellcome 2023 and McKinsey 2026 lists to this registry's row and tier, and gives the reason for every difference.

## 7. Limits

- **Re-review pending sign-off.** v1.2.0 applies the evidence-first re-review's proposals: 19 entries leave the strict cohort and 2 join it (49 → 32). They wait on the maintainer's sign-off and a 24-hour gate before the site shows them (`docs/REVIEW-SIGNOFF.md`).
- **Attribution is mostly self-reported.** 31 of 32 strict entries rest on the developer's or partner's own words. The protocol checks that the developer claims the AI did a named step, not that it did. How much the AI did cannot be verified from outside the company.
- **Second coding covers inclusion, not precedence.** Inclusion tiers were coded by two blind coders and a red team. Target precedence calls are still one coder's judgement under a written rule.
- **Registry coverage is uneven.** China CTR and jRCT are harder to search than ClinicalTrials.gov; recent first-in-human starts may be missing.
- **Survivorship.** Developers announce entries more readily than exits. Status is checked against registries where possible, but a quiet discontinuation can look like `unknown`.
- **Not an efficacy ranking.** Inclusion says nothing about whether a molecule works.

## 8. Updates

Quarterly refresh of status and new entries, plus corrections as they arrive. Each release is tagged and logged in `CHANGELOG.md`.

Every row carries a `last_verified` date: the day each of its fields was last checked against primary sources. The evidence is in `data/audit-log.csv`. It has one line per row and field, with the verdict (confirmed, changed or flagged), the old and new value, the source URL and a short verbatim quote. The log is append-only, so a later check adds lines and keeps the earlier ones. The first full field-by-field audit covered every row on 20 October 2026.
