# Changelog

## v1.1.13 — 2026-10-20
Field-by-field audit of every row against primary sources, with a per-row verification date and a public evidence log. Data now as of 20 October 2026.

**Count change: one strict molecule is approved.** The FDA approved lirafugratinib (RLY-4008, Lyrfigtu; Relay, licensed to Elevar) on 23 September 2026 for previously treated FGFR2 fusion or rearrangement cholangiocarcinoma, on the single-arm REFOCUS trial (NCT04526106) ([FDA](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-lirafugratinib-previously-treated-unresectable-locally-advanced-or-metastatic)). Its furthest phase is now "Approved (FDA 2026)". Approved strict molecules go from 0 to 1. The site headline, previously the fixed text "None is approved", is now computed from the data and reads "One is approved". The strict count (55), status split (40 ongoing, 15 stopped), precedence counts and Phase 2+ count (12) are unchanged. No inclusion tier, attribution tier or precedence category was changed.

- **Audit trail** (see `docs/DECISIONS.md`, METHODOLOGY § 8):
  - New `data/audit-log.csv` holds 1,672 lines, one per row and field: 1,235 confirmed, 351 changed, 86 flagged. Each line gives the source URL and a verbatim quote of 25 words or fewer.
  - Every cited page was fetched again and its quote matched: by script where the site allows it, otherwise by reading the page.
  - New `last_verified` column on `molecules.csv`, `candidates.csv` and `excluded.csv`, shown in each entry's expanded view as "Last verified" with a link to the log.
  - `excluded.csv` gains an `id` column.
- **Method:**
  - A ClinicalTrials.gov pre-pass searched every alias, by intervention and full text, plus each developer as sponsor, and compared the hits with `registry_ids`.
  - Research agents then checked each row against registries (ClinicalTrials.gov, ANZCTR, jRCT, China CTR/ChiCTR, EU CTIS, ISRCTN), the developer's and current owner's disclosures, filings and papers.
  - An independent verifier tried to refute every proposed change: 380 upheld, 43 amended, 4 refuted.
- **Identity and aliases** (23 rows): new INNs zilemaltib (SGR-1505), surbinsertib (SGR-3515), rexaceract (GT-02287), rocavorexant (INDV-2000), nuvustotug (HFB301001), emunkitug (HFB200301), muzastotug (ADG126) and zirdafulven (LP-184). New partner codes:
  - RO7517834 (migoprotafib)
  - DDY391 (MRT-6160, Novartis)
  - JNJ-31001074 (bavisant)
  - AMG 986 (azelaprag)
  - OSU-HDAC42 (REC-2282)
  - CHM-0033029 (CHM-029)
  - EVAX-01-CAF09b (EVX-01)
  - SYN-001 (fasoracetam)
  - S241656 (BDTX-4933, excluded)

  CEL383 = ABBV-8736 now rests on AbbVie's EU CTIS record (2024-513009-30-00), not on drug databases.
- **Developer and partner** (17 changes):
  - AO-252 licensed to Coiled Therapeutics (2026).
  - HMBD-002 licensed to Percheron Therapeutics (2025).
  - Genentech ended the migoprotafib licence (Jan 2025).
  - Exscientia bought GT Apeiron's share of GTAEXS-617 (Jul 2024).
  - NL-201 is now with Neurogene; SNX-281 with Stingthera.
  - Bavisant's originator is Johnson & Johnson, not Takeda.
- **Registry IDs** (49 rows): added missing ClinicalTrials.gov, EU CT, jRCT, China CTR and ISRCTN numbers. VRG50635's first-in-human study is ISRCTN14792372, and GT-02287's is ACTRN12623000860662. EU CT and ISRCTN numbers now link on the site.
- **First-in-human** (20 rows, detail and dates):
  - BEN-2293 (strict) moves from 2020 to 2021. BenevolentAI announced first dosing on 11 Feb 2021; the registry start date of Oct 2020 is kept in the detail.
  - Legacy borderline compounds now use the year of first dosing by any sponsor, as REC-4881 already did: BEN-2001 1942 → 2007, REC-994 2022 → 2004, REC-2282 2022 → 2010, azelaprag 2016.
  - OC514 now has a year: 2022.
- **Status detail** (41 rows) now gives the reason and date for each stop where a source states one. Borderline status changes, none of which moves a strict count:
  - NDI-101150 and GB-7624 ongoing → stopped: deprioritized, dropped from the developer's pipeline.
  - HST-1011 ongoing → unknown: no update since Nov 2024.
  - Omilancor unknown → ongoing; NIM-1324 stopped → ongoing. NImmune presented new data in 2026.
  - HMBD-002 stopped → ongoing (licensee plans a Phase 2), SLATE stopped → ongoing (NCI trial active), baricitinib stopped → ongoing (approved and marketed, coded like BXCL-501).
  - Borderline furthest phase: HMBD-001 Phase 1/2 → Phase 2; NECVAX-NEO1 Phase 1 → Phase 1/2.
- **Other fields:**
  - AI-role wording (25 rows), corrected to what the developer actually says.
  - Indication (40 rows): more precise, and US spelling.
  - Targets: SIGX1094 FAK/SRC, PHI-101 FLT3; CHK2, SOM3355 multimodal.
  - Six precedence bases: anachronistic or inaccurate wording fixed; no category changed.
  - Sources (87 rows): dead or non-supporting links replaced, primary sources added.
- **Notes:** internal process notes were removed from `notes`, `precedence_basis`, `inclusion_note` and the excluded reasons (backlog item).
- **Excluded rows:** 14 of 37 re-verified; their reasons still hold, with factual refreshes for REC-7735, inhaled rentosertib, ISM3312, SYH2070 and the Nuritas/Gubra row. The other 23 rows keep their reasons, but their `last_verified` is blank until a second search pass, because the audit hit its per-session web-search limit.
- `scripts/fetch_trials.py` now splits aliases on closing brackets too. Trials re-pulled: still 83 records for 47 strict molecules; none changed.

## v1.1.12 — 2026-10-20
Site only. No change to any count, inclusion or coding call.
- Source links in the registry's expanded view are named instead of numbered. Registries show their ID, for example "ClinicalTrials.gov NCT06548542". Other sources show the publisher, for example "Sumitomo Pharma", "SEC filing" or "Business Wire press release". Hovering a link shows the full URL.

## v1.1.11 — 2026-10-20
Trials re-pulled from ClinicalTrials.gov (API v2) on 20 October 2026; registry expanded view reworked. No change to any count, inclusion or coding call.
- `trials.csv`: 83 records for 47 strict molecules, up from 80. The three new records are the ABBV-8736 trials linked to CEL383 in v1.1.4: NCT06548542 (Phase 2, recruiting), NCT07141199 and NCT07413133 (Phase 1, completed). CEL383's next data due is now January 2030, where it previously read "no active trial". No existing trial changed status.
- Expanded view in the registry:
  - It repeats every headline column with more detail: furthest phase with first dosing, status, target type with its basis, and modality.
  - Next data due names the trial and whether its date is estimated or actual. When there is no date, it says why.
  - A ClinicalTrials.gov table lists each trial with a link, title, phase, status, start, primary completion and sponsor.
- The "next data due" cell wraps instead of truncating, and now reads "no active trial on ClinicalTrials.gov" when empty.
- The site revalidates its data files on every load, so readers always get the current release.

## v1.1.10 — 2026-10-20
Site only. No change to any count, inclusion or coding call.
- "Why other counts are bigger": each published count now links to its source by DOI, with numbered references under the chart. The references are Jayatunga et al. 2024 (75), Greenblatt & Geoui 2026 on Zenodo (83) and Haque et al., ASCO 2026 (117). Each figure was checked against its source on 20 October 2026. "This registry" links to the definition.
- METHODOLOGY § 6 links the same three sources.

## v1.1.9 — 2026-10-20
Site only. No change to any count, inclusion or coding call.
- Links to other sites (sources, registries, papers, GitHub) now open in a new tab on every page, so readers stay on the registry. Links within the site are unchanged.

## v1.1.8 — 2026-10-20
Site only. No change to any count, inclusion or coding call.
- "The question" chart: each published benchmark study has its own colour and marker shape, with a legend ordered by data period. Shapes keep the studies apart for colour-blind readers and in print. The markers are drawn faintly, so the AI estimate and the industry median lead.
- AI estimates are labelled in the journal convention, for example "48% (95% CI 30–67%)".

## v1.1.7 — 2026-10-20
Site only. No change to any count, inclusion or coding call.
- The top navigation now stays at the top of the screen on every page, and on phones it fits on one line. Section links land below it.

## v1.1.6 — 2026-10-20
Site only. No change to any count, inclusion or coding call.
- "The question" chart is now a forest plot.
  - Industry benchmarks are shown as the range of five published all-indication estimates, with each study marked and their median labelled at its line: DiMasi et al. 2016, Hay et al. 2014, BIO 2016, Wong et al. 2019 and BIO 2021. The page previously showed BIO 2021 alone.
  - The AI cohort's share that moved on is shown with a 95% CI whisker and labelled at its dot.
  - The scale is labelled 0–100%, with gridlines.
- The median Phase 1 to Phase 2 benchmark is now 63% (range 52–66%), up from the single BIO 2021 figure of 52%.
- The table view adds the per-study benchmark figures, and the notes explain why Wong et al. report a higher Phase 2 rate.

## v1.1.5 — 2026-10-20
Site only. No change to any count, inclusion or coding call.
- New page, "The question" (`question.html`, in the site navigation). It sets out why the registry exists: does AI change the odds that a drug makes it through clinical trials?
- The page shows each phase transition for the strict cohort: molecules that moved on, stopped or are still running. It sets the share that moved on (95% Wilson interval) against industry rates for 2011–2020 (BIO, Informa and QLS, 2021).
- A rate is shown in grey and not compared until at least 10 molecules have an outcome at that step; today that greys out Phase 2.
- Every figure on the page is computed from the data, so it updates with each release.

## v1.1.4 — 2026-10-20
Inclusion calls on the 13 October candidates, decided by the maintainer under the current definition. **Strict 54 → 55**; borderline 55 → 60; candidates 7 → 1.
- **ENV-308 → strict.** Enveda states that "ENV-308 was discovered using PRISM, Enveda's proprietary AI model" (18 August 2026). This is a molecule-specific claim of the kind that put ENV-294 in the strict cohort. First participant dosed in December 2025 (Enveda, 17 December 2025). Target undisclosed (`unclear`). Note: the parent metabolite, Lac-Phe, was characterized at Stanford without AI.
- **To borderline, platform-level attribution only:** MRT-2359, MRT-6160 and MRT-8102 (Monte Rosa's QuEEN engine) and JUV-161 (Juvena). All are dosed; none has a molecule-specific AI statement. Same rule as GB-7624.
- **To borderline, computational repurposing:** PXT3003 (Pharnext). Same rule as OC514.
- **ENV-6946 stays a candidate.** Phase 1 was "initiated" (December 2025), but no first-dosing statement has been found.
- **CEL383 → Phase 2, `ongoing`**, as AbbVie's ABBV-8736, which is in AbbVie's Phase 2 Crohn's platform trial NCT06548542. Strict Phase 2 or later goes 11 → 12. AbbVie does not name CEL383; the identity rests on drug databases and on AbbVie having a single anti-TREM1 asset. Confidence stays low.
- **iscartrelvir stays borderline.** Attribution moves from tier C to B: Westlake Laboratory itself says an ML model narrowed about 100 library hits to 9, including the approved molecule. The peer-reviewed design work is physics-based (docking, FEP), and the reason now says so.
- Strict status is now 40 ongoing, 15 stopped, 0 unknown. Precedented targets stay 37 of 51 disclosed.
- METHODOLOGY figures updated to match:
  - The uncertainty band is now about 55, −7/+8.
  - Definition sensitivity: 48 excluding physics-dominant platforms, about 61 counting all physics-based platforms, about 67 counting platform-level attribution (ENV-308 plus the four new platform-only entries).
  - Eight strict molecules have no ClinicalTrials.gov record.
- Site: the strict count in the comparison chart, the uncertainty note and the limits list is now computed from the data.
- Site: "Precedented" is now labelled "Known target" for general readers. The data value stays `precedented`.
- Site, census chart: dots stack in legend order from the bottom (precedented, novel, first-in-class, undisclosed). Precedented is a stronger blue, so it no longer blurs into undisclosed: normal-vision ΔE 10 → 22 (OKLab). Undisclosed is a pale neutral with a darker outline wherever it appears, which also keeps stopped-and-undisclosed rings visible.

## v1.1.3 — 2026-10-20
Source links checked. No change to any count, inclusion or coding call.
- All 151 source links in `molecules.csv` and `candidates.csv` were checked on 20 October 2026. Every one resolves. ClinicalTrials.gov links were confirmed through the API; pages that block automated requests were confirmed by fetching their content.
- Two citations did not support their row. AC0682 cited a release about AC0176; that link is removed, and the row keeps its ClinicalTrials.gov record. LP-184 cited a review supplement that does not mention it; this was fixed in v1.1.2.
- Two links in `candidates.csv` now use their canonical host (www).
- Every source added in v1.1.1 and v1.1.2 was checked the same way.

## v1.1.2 — 2026-10-20
Status re-check: every stopped, unknown and Phase 2+ entry checked against its registry (ClinicalTrials.gov API, ANZCTR, jRCT, China CTR) and the developer's latest disclosure, as of 20 October 2026. No change to any inclusion call or strict-cohort count.
- Strict, detail and sources only:
  - MDR-001: Phase 3 rests on MindRank's first-patient-dosed release (26 February 2026); the ClinicalTrials.gov record has not been updated since December 2025.
  - ABS-101: Absci's 12 November 2025 decision not to run later-stage trials itself, and the ANZCTR status.
  - ISM4808: removed registry ID "CTR20260301", which no source supports. Dosing rests on Insilico's 5 March 2026 release.
- Borderline status changes:
  - TG4050 `stopped` → `ongoing`: randomized Phase 2 fully enrolled, topline expected Q1 2028 (Transgene, April and September 2026).
  - GRANITE `ongoing` → `stopped`: sponsor bankrupt; assets sold to Seattle Project Corp on 30 December 2024 (SEC 8-K); no development disclosed since.
  - LP-184 `unknown` → `ongoing`: Phase 1a completed; Phase 1b/2 cleared by the EMA, July 2026. Its only source was a supplement that does not mention LP-184; replaced.
  - PHI-101 `unknown` → `ongoing`: Phase 1 completed; INN lasmotinib registered and a licensee sought, November 2025.
  - SOM3355 `unknown` → `ongoing`: FDA end-of-Phase 2 meeting agreed a Phase 3 design, September 2025.
  - fasoracetam `unknown` → `ongoing`: Synaptiq acquired NB-001 and plans a Phase 2b, July 2026. Highest phase corrected to Phase 2/3 (NCT02777931).
  - LAM-002A / LAM-001 `unknown` → `ongoing`: LAM-001 Phase 2 trials under IRulya (formerly Quince); developer chain updated.
  - ADG106 / ADG116 / ADG126 `stopped` → `ongoing`: ADG126 randomized Phase 2 ongoing, August 2026.
- Borderline corrections without a status change:
  - omilancor: highest phase corrected from "Phase 3 per Zenodo, unverified" to Phase 2; no Phase 3 is registered. Registry IDs added; it stays `unknown`.
  - OC514: detail added; stays `unknown`.
  - azelaprag: termination source and NCT06515418 added.
- Candidates, factual fields only; their tier is under review:
  - ENV-308: dosing confirmed 17 December 2025; Enveda's August 2026 molecule-specific AI statement recorded.
  - MRT-2359 and MRT-6160: now in Phase 2. MRT-8102: registry ID added.
  - JUV-161: now in Phase 1/2.
  - PXT3003: first in human 2010 (NCT01401257); China marketing application filed, April 2025.

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
