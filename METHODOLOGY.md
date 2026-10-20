# Methodology

Version 1.1.13 · data as of 20 October 2026

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

Six parallel searches: published seed lists (BCG/Jayatunga 2024 and successors); AI-native small-molecule developers in the US, Europe and Israel; Asia-Pacific developers and registries; biologics; pharma-internal assets; and an asset-agnostic registry and literature sweep. Results were merged and coded, then challenged by two independent passes: one trying to disprove entries (about 50 registry records re-checked) and one looking for missing assets. Searches were AI-assisted; every row carries its sources.

Trials (`trials.csv`) are every ClinicalTrials.gov record matched to a strict-cohort molecule by NCT number or verified intervention name (API v2, retrieved 20 October 2026). Eight strict molecules have no ClinicalTrials.gov record.

## 5. Uncertainty

The strict count is about **55, −7/+8**:
- dosing and attribution errors found by the verification pass: about ±2;
- assets probably missing, mainly from China CTR and recent US first-in-human starts: +0 to +6;
- definition sensitivity: excluding physics-dominant platforms gives 48; counting all physics-based platforms about 61; counting platform-level attribution about 67.

## 6. Other counts, and why they differ

| Count | Number | Definition |
|---|---|---|
| [Jayatunga et al. 2024 (BCG)](https://doi.org/10.1016/j.drudis.2024.104009), *Drug Discovery Today* | 75 | Clinical assets of AI-native companies since 2015 |
| [Greenblatt & Geoui 2026](https://doi.org/10.5281/zenodo.22814924) (Zenodo) | 83 | BCG list plus additions |
| [Haque et al., ASCO 2026](https://doi.org/10.1200/JCO.2026.44.16_suppl.11072) | 117 | "AI-enabled"; list not published |
| This registry | 55 | Molecule-level attribution, dosed in humans, written rules |

Lower is not more correct. Each count answers a different question; this one asks the narrowest.

## 7. Limits

- **Attribution is mostly self-reported.** 54 of 55 strict entries rest on the developer's statement. How much the AI did cannot be verified from outside the company.
- **Not second-coded.** Precedence calls are judgement under a written rule, made by one coder. Independent second coding is planned for v2.
- **Registry coverage is uneven.** China CTR and jRCT are harder to search than ClinicalTrials.gov; recent first-in-human starts may be missing.
- **Survivorship.** Developers announce entries more readily than exits. Status is checked against registries where possible, but a quiet discontinuation can look like `unknown`.
- **Not an efficacy ranking.** Inclusion says nothing about whether a molecule works.

## 8. Updates

Quarterly refresh of status and new entries, plus corrections as they arrive. Each release is tagged and logged in `CHANGELOG.md`.

Every row carries a `last_verified` date: the day each of its fields was last checked against primary sources. The evidence is in `data/audit-log.csv`. It has one line per row and field, with the verdict (confirmed, changed or flagged), the old and new value, the source URL and a short verbatim quote. The log is append-only, so a later check adds lines and keeps the earlier ones. The first full field-by-field audit covered every row on 20 October 2026.
