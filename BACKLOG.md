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
- Corrections form follow-ups: free forward `corrections@aixbio-registry.org` → John; Turnstile if spam appears; a daily scheduled check of the queue by Claude.
- Connect the Vercel project to GitHub so pushes deploy (needs the Vercel GitHub app; current remote uses an SSH alias the CLI cannot parse).
- v1 hardening (no definition change): close the six open checks from the 13 Oct rebuild; resolve the 7 candidates; re-check every stopped/unknown/Phase 2+ status against its registry; verify every source link; strip remaining internal process notes from `notes`.
- Add `modality_class` and `next_due` to the CSV/JSON so downloads carry what the site computes.
- v2.0 inclusion framework (contribution classes, decision log, shadow table, second coder): decide after launch.
