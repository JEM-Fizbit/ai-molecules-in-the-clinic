# Backlog

> Lightweight capture for ideas, bugs and small features. Newest at top, one line per item.
> Universal protocol: [ROADMAP_AND_BACKLOG.md](docs/protocols/ROADMAP_AND_BACKLOG.md). Decisions: `docs/DECISIONS.md`.

## Launch (with the AI × Bio essay)
- Flip repo public; set Vercel `ssoProtection` back to `all_except_custom_domains`; check https://aixbio-registry.org returns 200 logged out.
- Re-pull trials (`fetch_trials.py`), re-check EXS-21546 and the four Phase 3s; release note.
- Revoke the Vercel automation-bypass token `claude-smoke-test` (used for pre-launch testing).
- Set the Resend key and verify aixbio-registry.org in Resend if not done (form works without it; emails are skipped).

---

<!-- backlog items below; newest first -->
- Canonical address: make https://aixbio-registry.org canonical. Redirect www.aixbio-registry.org and ai-molecules-in-the-clinic.vercel.app to it (308, Vercel domain settings); add `<link rel="canonical">` and `og:url` to index.html and methodology.html; point README, CITATION and the cite line at the domain rather than the GitHub URL.
- Email channel for corrections (decided 20 Oct): turn on Resend Receiving for aixbio-registry.org (MX record) and add an inbound webhook endpoint that files each email to `corrections@aixbio-registry.org` into Neon `corrections` (same reference, review page and public log; replies to acknowledgements land there too). Verify the Resend webhook signature; strip quoted text; store sender as `submitter_email`; `source_url` may be empty for emailed items, so relax that constraint for this route only. Check Resend's receiving limits on the current plan first. Then show the address on the site as a second way to send a correction.
- Project-init leftovers: add this repo to the personal `project-docs-audit` scheduled task (read the task in full first; a partial `job_config` update wipes its prompt), and rebuild + republish the jem-registry Subscription Ledger for the new Neon/Resend rows.
- Email deliverability: corrections@ mail lands in Hotmail Junk while the domain is new; recheck in a few weeks; consider DMARC `p=quarantine` once sending is stable.
- Corrections form follow-ups: Turnstile if spam appears; a daily scheduled check of the queue by Claude.
- Connect the Vercel project to GitHub so pushes deploy (needs the Vercel GitHub app; current remote uses an SSH alias the CLI cannot parse).
- v1 hardening (no definition change): close the six open checks from the 13 Oct rebuild; resolve the 7 candidates; re-check every stopped/unknown/Phase 2+ status against its registry; verify every source link; strip remaining internal process notes from `notes`.
- Add `modality_class` and `next_due` to the CSV/JSON so downloads carry what the site computes.
- v2.0 inclusion framework (contribution classes, decision log, shadow table, second coder): decide after launch.
