# Methodology

Version 1.1.20 · data as of 20 October 2026

## 1. Definition

A molecule is in the **strict cohort** if all three hold:

1. **Material AI/ML role** in choosing the target or designing the molecule. Machine learning or generative methods did real work in target identification or molecule design, not only in screening logistics or general analytics.
2. **Attribution.** The developer or a first-tier source states that role for *this* molecule, not just for the company's platform in general.
3. **Dosed in humans** by the as-of date, in any registry (ClinicalTrials.gov, ANZCTR, jRCT, China CTR or equivalent) or per a dated developer announcement.

## 2. Inclusion tiers

| Tier | Meaning | Counted? |
|---|---|---|
| `strict` | Meets all three tests | Yes |
| `borderline` | Fails one test in a way reasonable people dispute: physics-based design with no ML claim; platform-level attribution only; secondary-source attribution only; AI-selected vaccine antigens; computational repurposing of an existing drug | No, but published with the reason in `inclusion_note` |
| `candidate` | Plausible but not yet verified | No |
| excluded | Considered and rejected (never dosed, in-licensed with no AI role, AI role disclaimed) | No; listed in `excluded.csv` |

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

## 4. How the list was built

Six parallel searches: published seed lists (BCG/Jayatunga 2024 and successors); AI-native small-molecule developers in the US, Europe and Israel; Asia-Pacific developers and registries; biologics; pharma-internal assets; and an asset-agnostic registry and literature sweep. Results were merged and coded, then challenged by two independent passes: one trying to disprove entries (about 50 registry records re-checked) and one looking for missing assets. Searches were AI-assisted; every row carries its sources. In October 2026 every stopped, unknown and Phase 2+ status was re-checked against its registry and every source link was verified (v1.1.2 and v1.1.3 in `CHANGELOG.md`).

Trials (`trials.csv`) are every ClinicalTrials.gov record matched to a strict-cohort molecule by NCT number or verified intervention name (API v2, retrieved 20 October 2026). Eight strict molecules have no ClinicalTrials.gov record. Posted protocols and statistical analysis plans are linked where the sponsor has uploaded them.

Approvals (`approvals` in `molecules.csv`) record each regulatory approval as agency, date, application or approval reference, indication and a link to the regulator's own record (Drugs@FDA for US approvals). A molecule can be approved and still `ongoing` when trials in other indications continue.

## 5. Uncertainty

The strict count is about **49, −2/+8**:
- dosing and attribution errors found by the verification pass: about ±2;
- assets probably missing, mainly from China CTR and recent US first-in-human starts: +0 to +6;
- definition sensitivity, each computed from `molecules.csv`:
  - excluding the remaining physics-dominant platform entries gives **47**: the strict cohort without the 2 Schrödinger entries (`sgr-1505`, `sgr-3515`);
  - counting all physics-based designs gives about **61**: adding the 12 borderline physics entries (`ndi-101150`, `ndi-219216`, `zasocitinib`, `firsocostat`, `snx-281`, `nl-201`, `gt-02287`, `sgr-2921`, `lirafugratinib`, `migoprotafib`, `rly-5836`, `zovegalisib`);
  - counting platform-level attribution gives about **63**: adding the 14 borderline platform-only entries (`gb-7624`, `gb-4362`, `ac699`, `ac0676`, `rly-8161`, `dptx3186`, `swa1211`, `df-003`, `mrt-2359`, `mrt-6160`, `mrt-8102`, `juv-161`, `env-6946`, `ao-252`).

The ±2 and +0 to +6 components come from the verification and completeness passes of the 13 October 2026 build; their working log is not yet published.

## 6. Other counts, and why they differ

| Count | Number | Definition |
|---|---|---|
| [Jayatunga et al. 2024 (BCG)](https://doi.org/10.1016/j.drudis.2024.104009), *Drug Discovery Today* | 75 | Clinical assets of AI-native companies since 2015 |
| [Greenblatt & Geoui 2026](https://doi.org/10.5281/zenodo.22814924) (Zenodo) | 83 | BCG list plus additions |
| [Haque et al., ASCO 2026](https://doi.org/10.1200/JCO.2026.44.16_suppl.11072) | 117 | "AI-enabled"; list not published |
| This registry | 49 | Molecule-level attribution, dosed in humans, written rules |

Lower is not more correct. Each count answers a different question; this one asks the narrowest.

## 7. Limits

- **Under re-review (October 2026).** Applying § 1.2 literally moved six strict entries to borderline in v1.1.15 and v1.1.20. All were counted on platform-level AI claims. One of them, lirafugratinib, had briefly been counted as an approved AI-derived drug. Every entry, strict, borderline and excluded, is being re-reviewed against a written evidence protocol, piloted first and cross-checked against other published lists, with the maintainer signing off each strict entry. Counts may change when it completes.
- **Attribution is mostly self-reported.** 48 of 49 strict entries rest on the developer's statement. How much the AI did cannot be verified from outside the company.
- **Not second-coded.** Precedence calls are judgement under a written rule, made by one coder. Independent second coding is planned for v2.
- **Registry coverage is uneven.** China CTR and jRCT are harder to search than ClinicalTrials.gov; recent first-in-human starts may be missing.
- **Survivorship.** Developers announce entries more readily than exits. Status is checked against registries where possible, but a quiet discontinuation can look like `unknown`.
- **Not an efficacy ranking.** Inclusion says nothing about whether a molecule works.

## 8. Updates

Quarterly refresh of status and new entries, plus corrections as they arrive. Each release is tagged and logged in `CHANGELOG.md`.

Every row carries a `last_verified` date: the day each of its fields was last checked against primary sources. The evidence is in `data/audit-log.csv`. It has one line per row and field, with the verdict (confirmed, changed or flagged), the old and new value, the source URL and a short verbatim quote. The log is append-only, so a later check adds lines and keeps the earlier ones. The first full field-by-field audit covered every row on 20 October 2026.
