# Backlog

> Lightweight capture for ideas, bugs and small features. Newest at top, one line per item.
> Universal protocol: [ROADMAP_AND_BACKLOG.md](docs/protocols/ROADMAP_AND_BACKLOG.md). Decisions: `docs/DECISIONS.md`.

## Essay launch day
The registry has been public since 20 Oct 2026, 09:15 (see `docs/DECISIONS.md`). Swapping the essay's links is handled on the Substack side. On the day:
- Re-pull trials (`fetch_trials.py` then `csv_to_json.py`); this picks up new NCTs such as ENV-294's Phase 2a trials.
- Re-check EXS-21546 and the four Phase 3s (rentosertib, zovegalisib, golukibart, MDR-001).
- Cut a release (CHANGELOG, version bump) and deploy.

---

<!-- backlog items below; newest first -->
- After John signs off the re-review (`docs/REVIEW-SIGNOFF.md` § D): apply the second-tier proposals as their own release. That means excluding the 9 borderline rows both coders would exclude, and adding full rows for GB-5267, BDTX-189/1535/4933, mRNA-4157, Gritstone CORAL, talabostat and BC-006 if approved. Then read CTR20230768 (ISM3312) and ChiCTR2600123936 (PAN-NeoVax) by hand. Update CLAUDE.md status.
- Audit loose ends after v1.1.16 (save point: `docs/AUDIT_HANDOFF_2026-10-20.md`): re-check the named sub-items in x-isomorphic-labs (Standigm, Syntekabio, Deargen, Elix, Shionogi), x-pharma-collaborations (Lilly, Bayer, Genentech Prescient, Astellas), x-abcellera-bamlanivimab (Teva/AbCellera, Adimab PM-1022, Entos, Gritstone COVID, HFB-30132A) and x-nuritas-peptides (Nuritas, Biogenea; Gubra pages returned 403), then set their `last_verified`. x-bd200 waits on the GB-5267 decision. Watch: Harbour BioMed LET003 (developer AI claim, undosed), BD200 NCT07797907 (start est. 31 Dec 2026), IAM217 (IND 30 Sep 2026). Still open: zasocitinib, baricitinib and BXCL-501 first-in-human years; ENV-6946 registry ID; OC514 components.
- Canonical address: 308 redirects from www.aixbio-registry.org and ai-molecules-in-the-clinic.vercel.app to https://aixbio-registry.org (Vercel domain settings). Add `<link rel="canonical">` and `og:url` to index.html and methodology.html. Point the cite line, README, CITATION and the GitHub repo homepage (`gh repo edit --homepage`) at the domain. Add robots.txt and sitemap.xml now that the site is indexable.
- Email channel for corrections (decided 20 Oct; see `docs/DECISIONS.md`). Check Resend's receiving limits on the current plan first.
  - Turn on Resend Receiving for aixbio-registry.org (MX record).
  - Add an inbound webhook that files each email to `corrections@aixbio-registry.org` into Neon `corrections`: same reference, review page and public log; replies to acknowledgements land there too.
  - Verify the webhook signature, strip quoted text and store the sender as `submitter_email`. Allow an empty `source_url` for this route only.
  - Then change the acknowledgement email's "This address does not receive replies" line and show the address on the site.
- Security:
  - Rate-limit or lock out repeated failed passwords on `/api/admin`.
  - Rotate the Neon `registry_web` password (it passed through a chat transcript once) and update `DATABASE_URL` in Vercel.
  - Never print secrets; pipe them from Keychain as CLAUDE.md § Operations describes.
- Connect the Vercel project to GitHub so pushes deploy. The CLI's git link failed on the `github-personal` SSH alias; use the Vercel GitHub app.
- Daily scheduled check of the corrections queue: Claude assesses each new item against its sources and METHODOLOGY.md and records an assessment. No status changes without John. Add Turnstile to the form if spam appears.
- Project-init leftovers:
  - Add this repo to the personal `project-docs-audit` scheduled task. Get the full trigger first, because a partial `job_config` update wipes its prompt.
  - Rebuild and republish the jem-registry Subscription Ledger for the new Neon and Resend rows.
- Email deliverability: corrections@ mail lands in Hotmail Junk while the domain is new. Recheck in a few weeks; consider DMARC `p=quarantine` once sending is stable.
- v1 hardening, remaining after v1.1.1–v1.1.4 (20 Oct): ask Haque/Veronesi (U Chicago) for the ASCO 117 list; strip remaining internal process notes from `notes`.
- Add `modality_class` and `next_due` to the CSV/JSON so downloads carry what the site computes.
- v2.0 inclusion framework (contribution classes, decision log, shadow table, second coder): decide after launch.
