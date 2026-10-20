# Registry audit: handoff and save point (2026-10-20)

**Read this first if you are a fresh session picking up the registry audit.** It covers the state after the field-by-field audit of 20 October 2026, v1.1.13 to v1.1.16. Standing rules are in `CLAUDE.md`, `METHODOLOGY.md` and `docs/DECISIONS.md` (entry "Per-row verification date and a field-level audit log"). Open work items are in `BACKLOG.md`; this document does not duplicate them.

## TL;DR

Every row was audited field by field against primary sources. The evidence is in `data/audit-log.csv` (1,783 lines, append-only). Each row carries a `last_verified` date.

- **Source state:** `main` holds v1.1.16, commit `9eb57ef` plus this save point, data as of 20 Oct 2026. Strict count is 53: 39 ongoing, 14 stopped. 12 reached Phase 2 or later, 4 are in Phase 3 and 1 is approved (lirafugratinib, FDA 23 Sep 2026).
- **Live state:** https://aixbio-registry.org runs **v1.1.14**, where strict is still 55. v1.1.15 holds the maintainer decisions (strict 55 → 53) and v1.1.16 the second audit pass; **neither is deployed**. Deploying needs John's approval and the QA gate in `CLAUDE.md`.

## 1. What is done (verified)

| Release | Content |
|---|---|
| v1.1.13 (`24ac8b2`) | Field-by-field audit of all 153 rows. Adds `audit-log.csv`, `last_verified` on all three CSVs and an `id` on `excluded.csv`. The site shows "Last verified"; the approval headline is computed. Lirafugratinib becomes Approved. |
| v1.1.14 (`0fc9a9d`) | Traceability pass. The question page no longer counts an approval without a Phase 3 as passing Phase 3. **Live.** |
| v1.1.15 (`9d96916`) | John's decisions: AO-252 and SGR-2921 → borderline; ENV-6946 → borderline; ENV-294 (RAC2) and CLY-124 (DCN1) first-in-class. Tier A rule: developer-authored papers do not count. Strict 55 → 53. |
| v1.1.16 (`9eb57ef`) | Second pass: 18 more excluded rows verified (32 of 37 dated). HLX-1502, OC514 and INDV-2000 settled; registry IDs added for PAN-NeoVax, TG4050 and CLY-124. No count change. |

**Checks run:**
- Every cited URL was re-fetched and its quote matched: by script, or by reading pages that block bots through Firecrawl.
- An adversarial verifier reviewed every v1.1.13 change: 380 upheld, 43 amended, 4 refuted.
- Local site QA for v1.1.13: desktop light and 390 px dark screenshots, and no console errors apart from the expected local 404 on `/api/corrections-log`.
- Counts were checked against the README in v1.1.16.

## 2. Decisions still open (John)

- **ISM3312:** Insilico's Nat Commun 2025 paper credits Chemistry42 de novo design and reports a completed healthy-volunteer Phase 1 in China (CTR20230768). It stays excluded until decided; if included, it is likely strict.
- **GB-5267** (Generate/Roswell Park CAR-T, dosed 1 Oct 2026): does the registry cover cell therapies? `x-bd200` stays undated until this is decided.
- **Deploy** v1.1.15 and v1.1.16.
- Lower priority, from `audit-v1.1.13-decisions.md` in the session notes and not yet acted on:
  - Phase 1/2 precedence rule (HFB200301 vs HFB200603, MEN2312, BHB810).
  - Tier C → B on nine borderline rows.
  - Precedence fixes for firsocostat, LP-184, azelaprag and fasoracetam.
  - BEN-8744 stopped vs unknown.
  - GV20-0251 Phase 2.

  Check `CHANGELOG.md` v1.1.15 for any of these already applied.

## 3. Next task

Follow `BACKLOG.md`, "Audit loose ends after v1.1.16":
1. Re-check the named sub-items of `x-isomorphic-labs`, `x-pharma-collaborations`, `x-abcellera-bamlanivimab` and `x-nuritas-peptides`.
2. Set their `last_verified`.
3. Append the evidence lines.
4. Release as the next patch version.

Apply the ISM3312 and GB-5267 decisions once John makes them.

## 4. Invariants and gotchas

- **The audit log is append-only.** A recheck adds lines; never edit or delete old ones. Columns: `id, field, verdict, old_value, new_value, source_url, quote, checked_date`. Quotes are verbatim and 25 words or fewer, from a page actually fetched. Set `last_verified` only when every field of the row was checked.
- **Never change these without John:** inclusion tier, attribution tier or precedence category. Log a proposed change as `flagged` with a default instead.
- **WebSearch is capped at 200 calls per turn,** shared by every agent. v1.1.13 hit the cap. Prefer registry APIs (ClinicalTrials.gov v2, CTIS `ctis-public-api/retrieve/<EU CT>`) and known developer URLs. Fetching is not capped.
- **Sites that block bots:** Business Wire, GlobeNewswire, ir.recursion.com, sec.gov (which needs a declared User-Agent), ANZCTR and Fierce return 403 to curl and WebFetch. Firecrawl scrape reads them.
- Scratch tooling from v1.1.13 (pre-pass, URL and quote checker, apply script) lived in a session scratchpad and is **not in the repo**. Re-create it if needed; `scripts/fetch_trials.py` covers the ClinicalTrials.gov side.

### How to run

```bash
python3 scripts/csv_to_json.py
```
Run after any CSV edit. For `methodology.html`, use `python3 scripts/build_site.py`, which needs `markdown`; use a virtualenv. Preview locally with `python3 -m http.server 8765`. The deploy command is in `CLAUDE.md`; deploy only with John's approval.
