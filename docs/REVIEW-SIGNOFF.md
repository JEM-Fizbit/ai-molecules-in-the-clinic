# Re-review sign-off

_For John Milad. Branch `claude/evidence-rereview-527b3f`, release v1.2.0 (proposed). Nothing here is on `main` or the live site. Updated 20 Oct 2026 under [`REVIEW-PROTOCOL.md`](REVIEW-PROTOCOL.md) **v1.1**: the strict line is the acid test, and whether the claim says what the AI did is a flag (`ai_step_stated`)._

**Proposed strict count: 51** (now 49). 34 of them say what the AI did; 17 credit AI for the molecule without saying what it did. Compared with `main`, 8 entries leave the strict cohort and 10 join it. Two more molecules pass but are not rows yet (§ D). The contested calls put the plausible range at about 48–62.

## Decisions for you

**1. Approve the strict cohort in § A and the 8 moves out in § B?** Default: yes. Each row has two blind coders and a red team behind it. The 8 moves out:
- 4 have a physics-based design account: ATH-063, BBO-8520, SGR-1505, SGR-3515;
- 2 credit a platform that the statement does not call AI: BEN-2293, TOS-358;
- 2 fall to red-team evidence that the AI claim is contradicted: SIGX1094, VRG50635.

**2. Red-team calls on molecules that pass the acid test.** Each needs agree or overrule.

| Row | Proposed | Red-team evidence | Default and why |
|---|---|---|---|
| GT-02287 (rexaceract) | borderline `physics_only` | Gain's own 2025 paper: binding site from molecular dynamics, hits from docking 5 million compounds, no ML; "Magellan AI" is a 2026 rebrand of the physics-based SEE-Tx | **Borderline.** The developer's own detailed account contradicts the AI credit. |
| HLX-1502 | borderline `repurposing` | Healx's platform targets "clinically de-risked" opportunities; GEN reports prior healthy-volunteer safety data; its first trial is a Phase 2; no parent drug is named | **Borderline**, low confidence. The evidence is circumstantial. If HLX-1502 is a new chemical entity it becomes strict, with the AI step not stated. |
| HMBD-001 | borderline (proposed for exclusion, `legacy_retrofit`) | Hummingbird's 2017–21 pages describe the platform without ML; the tool was renamed mAbPredict → mAbPredictAI later | **Exclude** in the follow-up release. The fallback is borderline `physics_only`. |
| HFB301001 (nuvustotug) | borderline `platform_only` | HiFiBiO's 2026 paper: chosen from a droplet-microfluidic screen; AI was used afterwards to map the epitope | **Borderline.** AI came after the molecule was chosen. |
| PHI-101 | borderline `other` | Pharos licensed a candidate co-developed by KIST and DGMIF in 2016; the AI role described is hERG and ADMET filtering | **Borderline.** Origin contested; `in_licensed` if a KIST source turns up. |
| GS-0321 (COM503) | borderline `other` | IL-18BP was published as a checkpoint by Yale (Nature 2020) before Compugen disclosed it; "AI/ML-powered Unigen" wording appears only from 2025 | **Borderline**, low confidence. |
| VRG50635 | borderline `other` | PIKfyve in ALS came from a 2018 non-ML screen co-authored by Verge's founders | **Borderline.** Unchanged from v1.0. |

**3. The v1.0 contested calls, re-evaluated under the acid test:**
- **ISM4808 → strict** (AI step not stated): "empowered by … Chemistry42" credits a named AI tool.
- **DSP-0038 → strict** (AI step stated): "created using Exscientia's AI technologies".
- **BEN-2293 → borderline `platform_only`**: "The Benevolent Platform identified…" does not call the platform AI.
- **REC-1245 → strict.**
- **ATH-063, VRG50635 and GS-0321 → borderline,** on red-team evidence that has nothing to do with the materiality rule.

**4. Scope defaults** (protocol § 6): S1 GB-5267 → borderline `other`; S2 MTS105 stays excluded; S3 ISM3312 coded like any row, and strict.

**5. § D proposals** (no strict row changes on the branch): add BC-006/ADG125 and bebtelovimab as strict rows, then the borderline and exclusion changes. Default: a follow-up release.

**6. Your blind labels** on [`REVIEW-PILOT-PACK.md`](REVIEW-PILOT-PACK.md) are still to come. They are judged against the v1.1 strict line.

**Who does what:** you decide. The parent session merges `refs/heads/claude/evidence-rereview-527b3f` after your sign-off and the 24-hour headline gate, then deploys.

## A. The proposed strict cohort (51)

Each claim is quoted verbatim from the linked page. Every page was re-fetched and the quote found on it. Dosing was checked against ClinicalTrials.gov (actual start or actual enrolment), another registry, or a dated developer statement, as the note says. *(new)* marks an entry not strict on `main`.

| # | Molecule | Claim (verbatim) | By | AI step stated | Source | Note |
|---|---|---|---|---|---|---|
| 1 | ABS-101 | “Designed and optimized using our generative AI platform, ABS-101 exhibits high affinity and potency, expected low immunogenicity, and an extended dosing interval—all of which are intentional attributes achieved through AI.” | developer, 2025-05 | yes (design) | [link](https://investors.absci.com/news-releases/news-release-details/absci-announces-first-participants-dosed-phase-1-clinical-trial) |  |
| 2 | ABS-201 | “ABS-201, an AI-designed Antibody, Blocks Prolactin/PRLR Signaling and Presents a Novel Biologic Strategy for the Treatment of Androgenetic Alopecia” | developer, 2026-08 | yes (design) | [link](https://www.sec.gov/Archives/edgar/data/1672688/000167268826000134/exhibit991-2026q210xqpr.htm) |  |
| 3 | AC0176 | “The initiation of this study marks the second program from our AI-enabled drug discovery platform and our chimeric degrader portfolio to enter the clinic” | developer, 2022-03 | no | [link](https://www.businesswire.com/news/home/20220330005709/en) |  |
| 4 | AC0676 *(new)* | “Leveraging our protein crystallography and AI-empowered PPI-TAC (Protein-Protein Interaction Targeting Chimera) platforms, AC0676 was designed to potently and selectively degrade both wildtype BTK and BTK mutations” | developer, 2023-06 | no | [link](https://www.biospace.com/accutar-biotechnology-announces-first-patient-dosed-with-ac0676-in-phase-1-study-in-patients-with-relapsed-refractory-b-cell-malignancies) |  |
| 5 | AC0682 | “it marks the first program from our AI-enabled drug discovery platform and our chimeric degrader portfolio to enter the clinic” | developer, 2021-12 | no | [link](https://www.biospace.com/accutar-biotechnology-announces-first-patient-dosed-with-ac0682-in-phase-1-study-in-patients-with-er-positive-her2-negative-locally-advanced-or-metastatic-breast-cancer) |  |
| 6 | ADG106 *(new)* | “show the power of our AI-powered DPL platform not only in creating novel ADG106 and ADG116 NEObodies in targeting different epitopes of a given antigen” | developer, 2021-04 | no | [link](https://www.sec.gov/Archives/edgar/data/1818838/000110465921055911/a21-12293_120f.htm) | One entry for three antibodies (ADG106, ADG116, ADG126) |
| 7 | AU-409 *(new)* | “With the first patient dosed in our Phase 1 clinical trial for liver cancer, we take one step closer to helping these patients and proving the AI platform that discovered AU-409 will generate more novel treatments” | developer, 2023-09 | no | [link](https://www.auransa.com/pr-first-patient-dosed-phase-1-clinical-trial) | Partner filing: "a novel compound discovered and developed by Auransa" |
| 8 | BEN-8744 | “Our AI powered drug-discovery platform identified PDE10 as a novel target for UC, with no prior direct associations linking it in scientific literature.” | developer, 2023-08 | yes (target) | [link](https://www.businesswire.com/news/home/20230830333577/en/BenevolentAI-Doses-First-Participants-in-Clinical-Trial-of-BEN-8744-Targets-PDE10-an-AI-derived-Novel-Target-for-the-Treatment-of-Ulcerative-Colitis) |  |
| 9 | BHB810 | “our pipeline of BigHat-designed therapeutics, beginning with BHB810, one of the first AI-designed biologics to reach the clinic” | developer, 2026-09 | yes (design) | [link](https://www.bighatbio.com/news/bighat-biosciences-announces-75-million-series-c-financing) |  |
| 10 | BRY10 | “BRY10 marked the first project to enter the clinical development stage, which utilized Chugai’s proprietary AI-based antibody drug discovery support technology, MALEXA” | developer, 2025-01 | no | [link](https://www.chugai-pharm.co.jp/english/news/detail/20250130170004_1134.html) | May have been discontinued (absent from Chugai's Jun 2026 pipeline) |
| 11 | CEL383 | “Our first therapeutic candidate is an anti-TREM1 antibody for the treatment of inflammatory bowel disease (IBD). TREM1, a myeloid target with a central role in IBD, was identified through machine learning-enabled analysis of hundreds of clinical samples.” | developer, 2023 | yes (target) | [link](https://web.archive.org/web/20240104151254id_/https://celsiustx.com/) | TREM1 was linked to IBD before Celsius |
| 12 | CHM-029 | “CHARM has used its proprietary AI platform ... to specifically design CHM-029 to address this issue” | developer, 2026-10 | yes (design) | [link](https://www.globenewswire.com/news-release/2026/10/07/3376361/0/en/charm-therapeutics-announces-first-patient-dosed-and-first-cohort-fully-enrolled-in-its-phase-i-ii-clinical-trial-of-chm-029-for-acute-myeloid-leukemia.html) |  |
| 13 | CLY-124 | “It was created from Cellarity's proprietary drug discovery platform, through which single-cell transcriptomics mapping and AI modeling revealed an undiscovered target controlling the Globin-Switching mechanism.” | developer, 2025-06 | yes (target) | [link](https://www.biospace.com/press-releases/cellarity-initiates-phase-1-clinical-study-of-cly-124-a-first-in-class-globin-switching-oral-medicine-for-the-treatment-of-sickle-cell-disease) |  |
| 14 | COM701 *(new)* | “Compugen continues to leverage Unigen™, its AI/ML-powered computational discovery platform, to identify novel drug targets and biological pathways grounded in human disease biology. Unigen has already discovered the targets of COM701, COM902, and GS-0321” | developer, 2026-08 | yes (target) | [link](https://s21.q4cdn.com/174215863/files/doc_earnings/2026/q2/earnings-result/CGEN-Q2-2026-results-Press-Release.pdf) |  |
| 15 | DPTX3186 *(new)* | “The development candidate was discovered using Dewpoint’s fully automated, AI/ML-enabled state-of-the-art platform and proprietary chemical library.” | developer, 2024-10 | no | [link](https://dewpointx.com/dewpoint-therapeutics-announces-nomination-of-first-c-mod-development-candidate-dptx3186-for-treatment-of-wnt-driven-cancers/) | Dosing per a dated developer release; registry start is estimated |
| 16 | DSP-0038 | “DSP-0038 is the third molecule created using Exscientia’s Artificial Intelligence (AI) technologies to enter clinical trials.” | developer, 2021-05 | yes (design) | [link](https://www.businesswire.com/news/home/20210513005059/en/Exscientia-Announces-Second-Molecule-Created-Using-AI-From-Sumitomo-Dainippon-Pharma-Collaboration-to-Enter-Phase-1-Clinical-Trial/) | Dosing rests on filings and a pipeline listing; no registry record |
| 17 | DSP-1181 | “We are proud that our AI drug discovery platform ... has contributed to generate DSP-1181” | developer, 2020-01 | yes (design) | [link](https://www.sumitomo-pharma.com/news/assets/pdf/ene20200130.pdf) | Dosing rests on Sumitomo statements; no registry record |
| 18 | DSP-2342 | “With three AI-generated development compounds designed for Sumitomo Pharma, plus our own emerging pipeline, we have repeatedly validated our approach” | developer, 2023-05 | yes (design) | [link](https://www.biospace.com/exscientia-announces-sixth-molecule-created-through-generative-ai-platform-to-enter-clinical-stage) | Quote covers three Sumitomo compounds, in a release about DSP-2342; dosing rests on filings |
| 19 | ENV-294 | “is the first drug candidate to advance to clinical trials based off of a molecule discovered in nature using AI and adapted with modern medicinal chemistry” | developer, 2024-11 | no | [link](https://www.businesswire.com/news/home/20241113334257/en/Enveda-Announces-First-Candidate-Discovered-From-Nature-Using-AI-Advances-to-Clinical-Trials) |  |
| 20 | ENV-308 | “ENV-308 was discovered using PRISM , Enveda’s proprietary AI model for finding naturally occurring and biologically active molecules already present in our bodies or our environment.” | developer, 2026-08 | no | [link](https://enveda.com/news/308-phase1/) | Parent metabolite's role was published by Stanford in 2022; Enveda credits PRISM with the rest |
| 21 | EXS-21546 | “We originated the first three AI-designed precision drug candidates to enter human clinical trials. Among these is our most advanced internally developed drug candidate, EXS21546.” | developer, 2021-10 | yes (design) | [link](https://www.sec.gov/Archives/edgar/data/1865408/000110465921122290/tm2119783-17_424b4.htm) |  |
| 22 | EXS-4318 | “Expert drug hunters using the Company’s AI generative design platform identified EXS4318 within 11 months after initiating design and was the 150th novel compound synthesised in this programme.” | developer, 2023-02 | yes (design) | [link](https://www.businesswire.com/news/home/20230201006024/en/) | Dosing rests on Exscientia filings; no registry record |
| 23 | EXS-73565 | “Exscientia utilised generative design, machine learning and molecular dynamics approaches to precision-design ‘565, a potent and selective allosteric MALT1 inhibitor” | developer, 2023-10 | yes (design) | [link](https://www.businesswire.com/news/home/20231016372855/en/Exscientia-to-Present-New-Preclinical-Data-for-AI-designed-LSD1-and-MALT1-Inhibitors-at-ESMO-2023) |  |
| 24 | EXS-74539 | “REC-4539, an AI-designed, LSD1 inhibitor, highlights early progress for a differentiated approach to targeting epigenetic drivers in cancer.” | developer, 2026-05 | yes (design) | [link](https://www.sec.gov/Archives/edgar/data/1601830/000160183026000077/exhibit991-q0126.htm) |  |
| 25 | garutadustat | “ISM5411, a potentially first-in-class PHD 1/2 inhibitor for the treatment of inflammatory bowel disease (IBD) designed by its generative AI platform.” | developer, 2023-12 | yes (design) | [link](https://www.eurekalert.org/news-releases/1010336) |  |
| 26 | GB-0669 | “Generative, ML-guided optimization was used to improve potency and developability while preserving epitope breadth.” | developer, 2025 | yes (design) | [link](https://generatebiomedicines.com/media-center/first-in-human-results-for-gb-0669-durable-neutralization-from-an-ai-designed-antibody) |  |
| 27 | golukibart | “GB-0895 is an antibody optimized using AI to achieve ultra-high-affinity TSLP binding, extended half-life, and high specificity.” | developer, 2025-12 | yes (design) | [link](https://kyodonewsprwire.jp/release/202512010151) | Half-life came from a standard Fc change; the affinity work was AI |
| 28 | GTAEXS-617 | “This underlines our confidence that we have not only used AI to design a potent and selective compound, but one that has balanced overall properties” | developer, 2024-07 | yes (design) | [link](https://www.businesswire.com/news/home/20240718738353/en) |  |
| 29 | GV20-0251 | “GV20-251 is the first clinical stage, AI-designed antibody therapeutic against an AI-predicted target in the clinic.” | developer, 2026-03 | yes (design) | [link](https://digital-release.wowktv.com/business/press-releases/cision/20260317NE10166/gv20-therapeutics-announces-late-breaking-oral-presentation-of-gv20-0251-translational-findings-at-the-aacr-annual-meeting-2026) | Target half unsupported (own paper credits CRISPR screens); counted for design |
| 30 | HFB200301 *(new)* | “advanced AI/ML-based data analytics to gain unprecedented insights into human disease biology. Through the platform, HiFiBiO Therapeutics has advanced 8 programs to clinical candidate selection, including three programs that are currently in Phase 1 trials, a first-in-class TNFR2 agonist (HFB200301” | developer, 2023-11 | no | [link](https://hifibio.com/hifibio-therapeutics-drug-intelligence-science-dis-platform-wins-ai-innovation-of-the-year-in-2023-biotech-breakthrough-awards/) | Low confidence: credits a microfluidics-plus-AI platform; a sibling antibody (HFB301001) was found by a non-AI screen |
| 31 | HMBD-002 *(new)* | “We also applied machine learning algorithms, such as PRISM, to identify 25 low energy template interfaces overlapping with the PD1-PDL1 interface” | developer's paper, 2022-02 | no | [link](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8823246/fullTextXML) | Antibody came from immunisation; the developer's paper credits ML for choosing the epitope |
| 32 | IAM1363 | “Covalent pan-mutant inhibitor, discovery driven by ML coupled with microscale HTE” | developer, 2026-10 | no | [link](https://www.sec.gov/Archives/edgar/data/1997038/000119312526417416/iam-20261008.htm) |  |
| 33 | imneskibart | “AU-007 is a human IgG1 monoclonal antibody designed using artificial intelligence to harness the power of interleukin-2 (IL-2) to eradicate solid tumors.” | developer, 2023-12 | yes (design) | [link](https://www.biospace.com/aulos-bioscience-advances-au-007-to-phase-2-portion-of-phase-1-2-study-evaluating-computationally-designed-il-2-antibody-for-treatment-of-solid-tumors) |  |
| 34 | ISM3091 | “The novel structure of ISM3091 was designed and optimized using Insilico's proprietary AI platform, Chemistry42” | developer, 2023-05 | yes (design) | [link](https://sciencesources.eurekalert.org/news-releases/990417) |  |
| 35 | ISM3312 *(new)* | “We utilize the advanced generative chemistry platform Chemistry42 for de novo molecular design and obtained novel small-molecule, non-peptide-like inhibitors targeting the SARS-CoV-2 Mpro. ISM3312 is identified as an irreversible, covalent Mpro inhibitor” | developer's paper, 2025-05 | yes (design) | [link](https://www.nature.com/articles/s41467-025-59870-4) | Dosing rests on the developer paper only (CTR20230768 not read) |
| 36 | ISM3412 | “The molecule was designed using ligand-based AI-enabled drug design by Insilico’s generative chemistry application, Chemistry42” | developer, 2024-04 | yes (design) | [link](https://e3.eurekalert.org/news-releases/1042535) |  |
| 37 | ISM4808 | “the novel structure of ISM4808 was empowered by Insilico’s proprietary Chemistry42 engine, and was designed, synthesized, and tested” | developer, 2025-12 | no | [link](https://insilico.com/news/bei1suokn1-insilico-medicine-and-taigen-achieves-li) | Was contested in v1.0; both v1.1 coders pass it |
| 38 | ISM6331 | “Based on the novel scaffold generated by Chemistry42, ISM6331 is a highly novel molecule with best-in-class potential.” | developer, 2023-06 | yes (design) | [link](https://www.eurekalert.org/news-releases/991924) |  |
| 39 | ISM8207 | “Insilico Medicine together with Fosun Pharma proposed an oncology target hypothesis and designed the compound with favorable druggability by leveraging Pharma.AI, its generative AI-driven platform.” | developer, 2024-05 | yes (design) | [link](https://sciencesources.eurekalert.org/news-releases/1044804) |  |
| 40 | ISM8969 | “ISM8969, a potential best-in-class NLRP3 inhibitor, was discovered and optimized using Chemistry42, Insilico’s proprietary generative chemistry engine.” | developer, 2026-01 | yes (design) | [link](https://insilico.com/news/r6iax95rk1-insilico-medicine-and-hygtia-therapeutic) |  |
| 41 | JUV-161 *(new)* | “JUV-161 was discovered using Juvena’s proprietary JuvNET platform, an AI and stem cell secretome-based drug discovery and development platform” | developer, 2025-05 | no | [link](https://www.globenewswire.com/news-release/2025/05/19/3083992/0/en/Juvena-Therapeutics-Announces-Initiation-of-First-in-Human-Clinical-Trial-of-JUV-161.html) | Engineered fusion of a known human protein |
| 42 | MDR-001 | “the first patient has been dosed in the Phase III clinical trial of MDR-001, its AI-designed oral small-molecule GLP-1 receptor agonist (GLP-1RA)” | developer, 2026-02 | yes (design) | [link](https://www.mindrank.ai/en/news/detail/155) |  |
| 43 | MEN2312 | “MEN2312 was designed by Insilico’s R&D team with the help of its end-to-end Pharma Generative AI platform to inhibit KAT6” | partner, 2025-01 | yes (design) | [link](https://www.menarini.com/en-us/news/news-detail/menarini-group-and-insilico-medicine-enter-a-second-exclusive-global-license-agreement-for-an-ai-discovered-preclinical-asset-targeting-high-unmet-needs-in-oncology.html) |  |
| 44 | MEN2501 | “MEN2501, highly differentiated small molecule KIF18A inhibitor in development for chromosomally unstable solid tumors designed using Insilico’s generative AI engine.” | developer, 2026-02 | yes (design) | [link](https://insilico.com/news/g3l291v091-insilico-medicine-receives-usd-5-million) |  |
| 45 | PEP08 | “Leveraging XtalPi’s integrated quantum physics-, AI-, and robotics-powered platform, PEP08 was designed to overcome the dose-limiting hematological toxicities seen with first-generation PRMT5 inhibitors.” | partner, 2026-05 | no | [link](https://en.xtalpi.com/xtalpi-enabled-pharmaengine-pep08-achieves-enrollment-milestone-with-second-synthetic-lethality-program-underway/) |  |
| 46 | PQ203 | “PQ203, our most advanced AI-designed peptide-drug conjugate, is currently in a Phase 1 clinical trial in patients with advanced solid tumors, including those with triple-negative breast cancer.” | developer, 2026 | yes (design) | [link](https://www.proteinqure.com/pipeline) | Same release also says "rationally designed" |
| 47 | REC-1245 | “Recursion identified the novel regulatory role of RBM39 on CDK12 function using its AI-powered maps of biology.” | developer, 2024-12 | yes (target) | [link](https://ir.recursion.com/news-releases/news-release-details/recursion-announces-first-patient-dosed-phase-12-clinical-study) | Coders split in v1.0; passes on the red team's quote |
| 48 | REC-3964 | “Recursion discovered REC-3964 using its proprietary AI-powered drug discovery platform, the Recursion OS, in which machine learning is used to identify relationships between biological contexts and chemical entities.” | developer, 2022-09 | no | [link](https://www.sec.gov/Archives/edgar/data/1601830/000119312522243299/d319544dex991.htm) |  |
| 49 | rentosertib | “We identify TRAF2- and NCK-interacting kinase (TNIK) as an anti-fibrotic target using a predictive artificial intelligence (AI) approach. Using AI-driven methodology, we generated INS018_055, a small-molecule TNIK inhibitor” | developer's paper, 2024-03 | yes (both) | [link](https://www.nature.com/articles/s41587-024-02143-0) |  |
| 50 | RTX-117 | “The candidate, discovered and optimized using XtalPi’s AI + robotics platform alongside ReviR Therapeutics’ VoyageR AI platform” | partner, 2026-03 | no | [link](https://en.xtalpi.com/xtalpis-ai-robotics-platform-powers-first-clinical-milestone-for-revirs-rare-neurological-drug-rtx-117) |  |
| 51 | SWA1211 *(new)* | “SWA1211 is a highly potent and selective oral small-molecule HPK1 inhibitor, efficiently designed using the company's proprietary AI models.” | developer, 2025-06 | yes (design) | [link](https://www.stonewise.cn/197.html) |  |

## B. Moves out of strict (8)

| Molecule | Now | Why | Best claim found |
|---|---|---|---|
| ATH-063 | `physics_only` | Athos's G9a patent says its structures "were generated by computational molecular docking"; the G9a–IBD link was published in 2014 | “We used the Athos AI2 drug development platform to identify a previously unrecognized and novel therapeutic target, to create ATH-063” ([source](https://webdisclosure.com/press-release/athos-therapeutics-nasdaq-athos-announces-positive-topline-phase-1-data-for-its-ai-generated-novel-oral-g9a-inhibitor-ath-063-demonstrating-selective-expansion-and-activation-of-potent-anti-inflammatory-regulatory-t-cells-LLuE9EWu9iO)) |
| BBO-8520 | `physics_only` | LLNL's account credits an "AI- and physics-based" platform; the developer paper describes structure-based design with no ML | “the team behind this research initially synthesized only a few hundred compounds to discover BBO-8520 — using the AI- and physics-based LCADD platform to narrow down the number of possible successful small molecules for ” ([source](https://www.llnl.gov/article/51336/llnl-bridgebio-announce-trials-supercomputing-discovered-cancer-drug)) |
| BEN-2293 | `platform_only` | Credits "The Benevolent Platform", which the sentence does not call AI; BenevolentAI describes it as AI plus scientists and wet-lab data | “The Benevolent Platform™ identified the role of the Trk receptors as mediators of both itch and inflammation in atopic dermatitis.” ([source](https://www.benevolent.com/application/files/9716/7959/1440/BenevolentAI_Annual_Report_2022.pdf)) |
| zilemaltib | `physics_only` | Schrödinger's paper puts ML inside "physics-based modeling techniques" (FEP) | “By applying advanced physics-based modeling techniques, including combining free energy calculations with machine learning methods and a chemistry-aware compound enumeration workflow, extensive sets of de novo design ide” ([source](https://www.rcsb.org/structure/9mkc)) |
| surbinsertib | `physics_only` | Active-learning FEP+: physics-based free-energy design | “By combining FEP+ with high performance cloud computing and machine learning (Active Learning FEP+), over 9,000 FEP+ calculations were performed to evaluate the affinity of the most promising designs for inhibiting Wee1” ([source](https://www.schrodinger.com/life-science/learn/case-studies/high-precision-computationally-guided-discovery-highly-selective-wee1-inhibitors/)) |
| SIGX1094 | `platform_only` | Red team: Signet's founder nominated FAK for gastric cancer in a 2019 paper with no ML, a year before Signet was founded | “By combining the strengths of organoids and AI, Signet identified the FAK as a potential target for treating DGC.” ([source](https://www.businesswire.com/news/home/20250113674680/en)) |
| TOS-358 | `platform_only` | AI appears only in company boilerplate; Totus's releases describe the molecule without AI | “discovering novel covalent small molecules against previously undrugged or difficult-to-drug targets using its proprietary AI-powered OmniDEL platform. The company’s lead program, TOS-358, is the first and only covalent ” ([source](https://www.totusmedicines.com/article?url=totus-medicines-presents-phase-1a-clinical-data-for-tos-358-a-covalent-pi3ka-inhibitor-at-esmo-tat-2026)) |
| VRG50635 | `other` | Red team: PIKfyve inhibition in ALS came from a 2018 non-ML phenotypic screen co-authored by Verge's founders | “VRG50635 is a small molecule inhibitor of PIKfyve, a novel therapeutic target for amyotrophic lateral sclerosis (ALS) discovered by CONVERGETM, Verge’s all-in-human, AI-powered platform.” ([source](https://www.biospace.com/verge-genomics-initiates-first-in-human-dosing-in-phase-1-trial-of-vrg50635-a-novel-therapeutic-for-amyotrophic-lateral-sclerosis)) |

## C. The ladder

Counts are cumulative and computed from `molecules.csv`. The list columns show where each published list's entries fall in this registry (`data/crosswalk.csv`). The same table is on the site, built from the data, and in METHODOLOGY § 6; `scripts/check_counts.py` checks every number.

| Step | This registry | Jayatunga 2024 (75) | Greenblatt & Geoui 2026 (83) | Wellcome 2023 (72) | McKinsey 2026 (9) |
|---|---|---|---|---|---|
| Strict, AI step stated | **34** | 15 | 17 | 4 | 7 |
| Strict (acid test) | **51** | 22 | 25 | 11 | 8 |
| + platform-only | **67** | 31 | 34 | 15 | 8 |
| + physics-based | **86** | 44 | 49 | 23 | 9 |
| + repurposing, vaccines, other | **117** | 62 | 68 | 43 | 9 |
| Excluded here, or not in this registry | – | 13 | 15 | 29 | 0 |

- **Jayatunga (75) and Greenblatt & Geoui (83)** land between the platform-only step (67) and the physics-based step (86). Their totals sit close to this registry's count with physics-based design included. 22 and 25 of their entries are strict here.
- **Haque et al.'s 117** "AI-enabled" assets equal all of this registry's strict and borderline entries combined (117). Their list is unpublished, so their molecules cannot be placed.
- **McKinsey's nine** are 8 strict, 7 of them with the AI step stated. The ninth, SGR-1505, is physics-based.
- **The gap with the field is classification, not detection.** Only 4 of the lists' molecules are missing here (§ E).

## D. Proposals not applied on the branch

**New strict rows** (they pass under v1.1 and survived the red team; each needs a full row first):
- **BC-006 / ADG125:** "derived from" Adagene's AI-powered platform; Dragon Boat's first-in-human trial NCT05212896.
- **Bebtelovimab:** AbCellera and Lilly; ML ranked the screening hits; AI step not stated.

**Exclusions:**
- HMBD-001 (`legacy_retrofit`, Decision 2).
- 9 borderline entries both v1.0 coders would exclude:
  - `no_ai_link`: AC699, NDI-219216, NEU-723, RLY-8161;
  - `out_of_scope`: NEU-411;
  - `in_licensed`: fasoracetam, LP-184;
  - `legacy_retrofit`: COM902;
  - `not_dosed`: PAN-NeoVax (ChiCTR not read by me).

**Borderline additions:**
- GB-5267 (`other`, S1).
- Platform-only under v1.1: BDTX-189, silevertinib, BDTX-4933 (MAP engine), bamlanivimab and ABBV-295.
- `vaccine_antigen`: mRNA-4157, autogene cevumeran (one coder only) and Gritstone CORAL.
- Talabostat / BXCL-701 (`repurposing`).

## E. Numbers

**Pilot** (24 rows, protocol v0.9; [`REVIEW-PILOT.md`](REVIEW-PILOT.md)):
- tier agreement 23 of 24 (95.8%, κ = 0.93);
- keyed answers reproduced: 18 and 19 of 19;
- all six known fails caught blind.

**Full review** (158 rows, protocol v1.0):
- tier agreement 91.8% (κ = 0.87); strict versus not strict 98.1% (κ = 0.95);
- red team on 38 strict passes: 32 survive.

**v1.1 re-code** (47 platform-level cases, two fresh blind coders):
- acid-test agreement 47 of 47 (κ = 1.0);
- step-flag agreement 25 of 28 passes;
- red team on 28 passes: 21 survive.

**Quotes:** every quote written to the CSV was re-fetched and found on its page. That is 56 of 56 v1.1 claims: 50 by script, 6 by hand.

**Crosswalk** ([`data/crosswalk.csv`](../data/crosswalk.csv)):
- **Missing here:** 4 distinct assets, all researched.
  - BC-006 is a strict candidate.
  - Talabostat is borderline.
  - Tolcapone and prexasertib are excluded.
  - ADG-104 fails the acid test.
- **Extra:** 26 strict entries are on none of the three BCG-era lists. 23 were first dosed after Jayatunga's December 2023 cut-off. The other three are DSP-2342, GB-0669 and ISM3312; McKinsey lists the last two.

**Projected headline (v1.2.0):**
- strict 51: 41 ongoing, 10 stopped;
- 9 reached Phase 2 or later, 3 in Phase 3, none approved;
- known targets 31 of 46 disclosed (67.4%), 6 first-in-class;
- borderline 66;
- sensitivity: 70 counting physics-based design, 67 counting platform-only attribution.

## F. What I could not verify

- **ISM3312:** the China CTR record CTR20230768 is blocked to scripts. Dosing rests on Insilico's own paper, which says both "completed" and "being evaluated".
- **Dosing on developer statements only:** DSP-0038, DSP-1181, DSP-2342 and EXS-4318 have no registry record. ENV-308's dosing rests on Enveda's release (88 volunteers). CLY-124's PACTR record was not read.
- **PAN-NeoVax** ChiCTR record not read by me.
- **McKinsey 2026 Exhibit 2** is an image: transcribed from your PDF by the parent session, with its benchmark corrected (hit ID to PCC 32–50 months, then 16–20 months to FIH).
- **The Wellcome list** was transcribed from PDF text extraction, not checked against the rendered page.
- **Design accounts:** no paper or patent describing the design was found for MDR-001, SWA1211, EXS-74539, ABS-201, PQ203, AC0682, AC0176 or AC0676. These rest on the developer's claim alone, which v1.1 accepts.
- **Protocol deviation:** v1.1 was decided after the review, with its results in view. The pilot's agreement still covers the attribution, dosing and code rules; the step rule is now only a flag.
- **Not second-coded:** target precedence, status and phase.
- **A false positive in the approvals check:** `check_approvals.py` now limits repurposed entries to their own sponsors' approvals. It used to flag other companies' dexmedetomidine products against BXCL-501, depending on which 10 results the FDA API happened to return.
