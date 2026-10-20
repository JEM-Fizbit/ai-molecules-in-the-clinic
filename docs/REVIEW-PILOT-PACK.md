# Blind evidence pack for John (10 rows)

_Evidence only: no current tier, no coder verdict. Label each row **S** (strict), **B** (borderline) or **X** (excluded) under the rules in [`REVIEW-PROTOCOL.md`](REVIEW-PROTOCOL.md) § 3, before reading the pilot results. Reply with ten letters, for example `J01 S, J02 B, …`. Each quote was found on its page by the maintainer session's check._

Rules in one line each: (1) the developer or partner ties AI or ML to this molecule in its own words; (2) the claim says what the AI did: chose the target or designed the molecule; (3) dosed in humans by 20 Oct 2026; (4) no evidence that defeats 1–3.

## J01. lirafugratinib / RLY-4008 — Relay Therapeutics

- **AI claim** (developer, 2024-02-22): “We believe we have validated our Dynamo platform and approach with the encouraging interim clinical data for RLY-2608 and lirafugratinib that we have announced over the course of 2021 to 2023.” [source](https://www.sec.gov/Archives/edgar/data/1812364/000095017024018797/rlay-20231231.htm)
- **AI claim** (developer, 2022-09-11): “We believe the interim ORR of 88% for these patients helps to demonstrate the potential power of our Dynamo platform to build transformative therapies for patients.” [source](https://ir.relaytx.com/news-releases/news-release-details/late-breaking-data-presented-esmo-congress-2022-demonstrate)
- **Dosing:** “REFOCUS: A First-in-Human Study of Highly Selective FGFR2 Inhibitor, RLY-4008, in Patients With ICC and Other Advanced Solid Tumors” [source](https://clinicaltrials.gov/api/v2/studies/NCT04526106)
- **Evidence a sceptic would raise:** Same 10-K, lirafugratinib design account: 'We embarked on a process using computational methods such as long timescale molecular dynamics simulations, virtual docking and specialized experimental techniques to design, select, synthesize, and evaluate inhibitors.' Relay-authored PNAS 2024 discovery paper (PMID 38300868, https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=38300868&rettype=abstract&retmode=text) credits long-timescale molecular dynamics of the P-loops and never mentions ML. The 10-K's ML wording ('molecular dynamics, or MD, and machine learning, or ML, capabilities') is platform-level.
- **Your label:** 

## J02. MRT-2359 — Monte Rosa Therapeutics

- **AI claim** (developer, 2026-03-17): “MRT-2359 is a potent and selective GSPT1-directed MGD discovered and rationally designed using our QuEEN” [source](https://www.sec.gov/Archives/edgar/data/1826457/000119312526109360/glue-20251231.htm)
- **AI claim** (developer, 2022-10-24): “QuEEN™ Discovery Engine Facilitates the Discovery of MRT-2359” [source](https://www.sec.gov/Archives/edgar/data/1826457/000119312522267232/d412446dex991.htm)
- **Dosing:** “In mCRPC patients with AR mutations, treatment with MRT-2359 in combination with enzalutamide led to a 100% PSA response rate in all 5 patients identified as having AR mutations.” [source](https://www.sec.gov/Archives/edgar/data/1826457/000119312526109360/glue-20251231.htm)
- **Evidence a sceptic would raise:** QuEEN is a hybrid engine ('combines AI-guided chemistry, diverse chemical libraries, structural biology, and proteomics', Q2 2025 8-K https://www.sec.gov/Archives/edgar/data/1826457/000095017025104545/glue-ex99_1.htm), and the quote says 'rationally designed', itself listed as non-AI wording. In Nov 2021, when MRT-2359 was nominated, AI was described only at platform level as 'AI/machine learning-based target selection' (https://www.sec.gov/Archives/edgar/data/1826457/000119312521326406/d244737dex991.htm). GSPT1 is a known CRBN glue neosubstrate. No developer paper on MRT-2359's design exists to confirm what ML did.
- **Your label:** 

## J03. DSP-1181 — Exscientia (now Recursion) / Sumitomo Pharma

- **AI claim** (developer, 2020-01-30): “We are proud that our AI drug discovery platform Centaur ChemistTM has contributed to generate DSP-1181” [source](https://www.sumitomo-pharma.com/news/assets/pdf/ene20200130.pdf)
- **AI claim** (developer, 2020-01-30): “We are proud that our AI drug discovery platform ... has contributed to generate DSP-1181” [source](https://www.sumitomo-pharma.com/news/assets/pdf/ene20200130.pdf)
- **Dosing:** “As a result of Phase 1 study, not reach expected criteria” [source](https://www.sumitomo-pharma.com/ir/library/presentation/assets/pdf/eir20220131.pdf)
- **Evidence a sceptic would raise:** Headline wording is 'created using AI', and the joint release credits Sumitomo's monoamine GPCR know-how alongside the AI ('contributed to generate'), so the AI share is unquantified. Development discontinued after Phase 1 (Sumitomo, Jan 2022). No evidence the molecule predates the collaboration.
- **Your label:** 

## J04. CLY-124 — Cellarity

- **AI claim** (developer, 2025-06-26): “It was created from Cellarity's proprietary drug discovery platform, through which single-cell transcriptomics mapping and AI modeling revealed an undiscovered target controlling the Globin-Switching mechanism.” [source](https://www.biospace.com/press-releases/cellarity-initiates-phase-1-clinical-study-of-cly-124-a-first-in-class-globin-switching-oral-medicine-for-the-treatment-of-sickle-cell-disease)
- **Dosing:** “today announced that the first subject has been dosed in a Phase 1 clinical trial of CLY-124” [source](https://www.biospace.com/press-releases/cellarity-initiates-phase-1-clinical-study-of-cly-124-a-first-in-class-globin-switching-oral-medicine-for-the-treatment-of-sickle-cell-disease)
- **Evidence a sceptic would raise:** Cellarity's ASH 2025 release (https://cellarity.com/news_item/cellarity-presents-on-cell-state-correcting-pipeline-programs-for-sickle-cell-disease-and-myelofibrosis-at-2025-american-society-of-hematology-annual-meeting/) describes the DCN1 finding as coming from its 'integrated discovery platform' predicting HbF-enriching compounds, linked to neddylation inhibition, without naming ML at that step; no evidence the chemistry itself was AI-designed. Registry PACTR record not read.
- **Your label:** 

## J05. ISM3312

- **AI claim** (developer_paper, 2025-05-15): “We employed a state-of-the-art generative chemistry platform, Chemistry42, to carry out the de novo molecular design of novel small-molecule, non-peptide-like inhibitors of SARS-CoV-2 ... This large-scale virtual screening and structure-based optimization pipeline identified ISM3312” [source](https://www.nature.com/articles/s41467-025-59870-4)
- **AI claim** (developer_paper, 2025-05-15): “ISM3312 generated by a generative AI engine has demonstrated its broad-spectrum activity against human coronaviruses, including SARS-CoV-2, MERS-CoV” [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC12081877/)
- **Dosing:** “currently Phase I study in healthy volunteers has been completed in China” [source](https://www.nature.com/articles/s41467-025-59870-4)
- **Evidence a sceptic would raise:** In the paper, Chemistry42 first searched pre-filtered vendor stock for a primary hit, then 'the generative chemistry engine of Chemistry42 has been utilized to perform versatile hit expansion and optimization'. Structure-based optimization was also involved. The China CTR record (CTR20230768) was not read. Insilico's Feb 2023 IND release ('generated and designed with the support of ... Chemistry42') was read only as a reprint (https://www.azolifesciences.com/news/20230224/Insilico-Medicine-IND-application-for-first-generative-AI-designed-drug-for-COVID-19-approved.aspx).
- **Your label:** 

## J06. zilemaltib / SGR-1505 — Schrodinger

- **AI claim** (developer_paper, 2025-10-13): “By applying advanced physics-based modeling techniques, including combining free energy calculations with machine learning methods and a chemistry-aware compound enumeration workflow, extensive sets of de novo design ideas were explored to quickly identify a novel hit series.” [source](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=41078320&rettype=abstract&retmode=text)
- **Dosing:** “Study of SGR-1505 in Mature B-Cell Neoplasms” [source](https://clinicaltrials.gov/api/v2/studies/NCT05544019)
- **Evidence a sceptic would raise:** The same abstract frames the work as 'physics-based modeling' (FEP-led); ML is a component combined with FEP, so a red team could argue physics_only. Schrodinger Q4 2025 release (https://ir.schrodinger.com/press-releases/news-details/2026/Schrdinger-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx) mentions SGR-1505 without AI wording; AI/ML language there is platform-level.
- **Your label:** 

## J07. SGR-2921 — Schrodinger

- **AI claim** (developer, 2024-02-28): “Using our computational platform, we identified multiple tight-binding, selective, and novel CDC7 inhibitor series, and selected SGR-2921 as our development candidate.” [source](https://www.sec.gov/Archives/edgar/data/1490978/000149097824000018/sdgr-20231231.htm)
- **Dosing:** “We have initiated dosing in a Phase 1 clinical trial of SGR-2921” [source](https://www.sec.gov/Archives/edgar/data/1490978/000149097824000018/sdgr-20231231.htm)
- **Evidence a sceptic would raise:** The same 10-K calls the platform 'physics-based computational platform'; no Schrodinger text found naming ML for SGR-2921. Program discontinued Aug 2025 after two treatment-related deaths (https://s203.q4cdn.com/609444515/files/doc_news/Schrdinger-Announces-Discontinuation-of-SGR-2921-Program-2025.pdf); NCT05961839 terminated, 66 actual.
- **Your label:** 

## J08. BRY10 — Chugai Pharmaceutical

- **AI claim** (developer, 2025-01-30): “Furthermore, BRY10 marked the first project to enter the clinical development stage, which utilized Chugai’s proprietary AI-based antibody drug discovery support technology, MALEXA” [source](https://www.chugai-pharm.co.jp/english/news/detail/20250130170004_1134.html)
- **AI claim** (developer, 2025-11-27): “The antibody drug BRY10, which was created using MALEXA, Chugai’s proprietary antibody drug discovery support technology based on AI, has now started clinical Phase I trials for chronic disease” [source](https://www.chugai-pharm.co.jp/cont_file_dl.php?f=FILE_1_140.pdf&src=%5b%250%5d,%5b%251%5d&rep=139,140)
- **Dosing:** “A PHASE I STUDY OF BRY10 IN HEALTHY MALE ADULTS” [source](https://jrct.mhlw.go.jp/en-latest-detail/jRCT2051240123)
- **Evidence a sceptic would raise:** The only step-level claim (MALEXA used in lead optimization) is Fierce Biotech's paraphrase of an unnamed spokesperson, not a verbatim developer quote (https://www.fiercebiotech.com/biotech/chugai-drops-only-ai-assisted-antibody-pipeline-still-has-high-hopes-technology). BRY10 was dropped in January 2026 (Chugai FY2025 results presentation). Target and indication undisclosed.
- **Your label:** 

## J09. AC0682 / AC682 — Accutar Biotechnology

- **AI claim** (developer, 2021-12-01): “it marks the first program from our AI-enabled drug discovery platform and our chimeric degrader portfolio to enter the clinic” [source](https://www.biospace.com/accutar-biotechnology-announces-first-patient-dosed-with-ac0682-in-phase-1-study-in-patients-with-er-positive-her2-negative-locally-advanced-or-metastatic-breast-cancer)
- **Dosing:** “today announced the dose administration for the first patient in a Phase 1 study of AC0682” [source](https://www.biospace.com/accutar-biotechnology-announces-first-patient-dosed-with-ac0682-in-phase-1-study-in-patients-with-er-positive-her2-negative-locally-advanced-or-metastatic-breast-cancer)
- **Evidence a sceptic would raise:** No Accutar paper on AC0682's design (PubMed: none). Accutar's current site (news, publications, patients pages) no longer mentions AC0682. Both trials terminated: NCT05080842 21 actual, NCT05489679 6 actual.
- **Your label:** 

## J10. ENV-308 — Enveda

- **AI claim** (developer, 2026-08-18): “ENV-308 was discovered using PRISM, Enveda’s proprietary AI model for finding naturally occurring and biologically active molecules already present in our bodies or our environment.” [source](https://enveda.com/news/308-phase1/)
- **AI claim** (developer, 2026-08-18): “ENV-308 was discovered using PRISM, Enveda’s proprietary AI model for finding naturally occurring and biologically active molecules” [source](https://enveda.com/news/308-phase1/)
- **Dosing:** “In its first clinical trial, ENV-308 was extremely well tolerated across 88 healthy volunteers” [source](https://enveda.com/news/308-phase1/)
- **Evidence a sceptic would raise:** Same release: the parent metabolite Lac-Phe 'was characterized in 2022 for its role in exercise by Stanford’s Jonathan Long and colleagues', and 'Enveda engineered ENV-308' with no AI named for that step. Target is undisclosed.
- **Your label:** 
