# Backlog

> Lightweight capture for ideas, bugs and small features. Newest at top, one line per item.
> Universal protocol: [ROADMAP_AND_BACKLOG.md](docs/protocols/ROADMAP_AND_BACKLOG.md). Decisions: `docs/DECISIONS.md`.

## Launch (with the AI × Bio essay)
- Flip repo public; set Vercel `ssoProtection` back to `all_except_custom_domains`; check https://aixbio-registry.org returns 200 logged out.
- Re-pull trials (`fetch_trials.py`), re-check EXS-21546 and the four Phase 3s; release note.
- Swap essay links to aixbio-registry.org.

---

<!-- backlog items below; newest first -->
- Corrections form: form on site → Vercel function → Neon `corrections`; Resend notification to John + acknowledgement; honeypot + rate limit; password-protected review page; public Corrections log from `corrections_public`; Resend sending records on aixbio-registry.org; free forward `corrections@` → John; Vercel functions in lhr1.
- Connect the Vercel project to GitHub so pushes deploy (needs the Vercel GitHub app; current remote uses an SSH alias the CLI cannot parse).
- v1 hardening (no definition change): close the six open checks from the 13 Oct rebuild; resolve the 7 candidates; re-check every stopped/unknown/Phase 2+ status against its registry; verify every source link; strip remaining internal process notes from `notes`.
- Add `modality_class` and `next_due` to the CSV/JSON so downloads carry what the site computes.
- v2.0 inclusion framework (contribution classes, decision log, shadow table, second coder): decide after launch.
