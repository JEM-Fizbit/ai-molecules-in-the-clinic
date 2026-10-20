# AI Molecules in the Clinic — project instructions

Open registry of AI-derived drug candidates dosed in humans: CC BY 4.0 data, a static public site, and a corrections form with a private review queue. Personal project (JEM-Fizbit). Launches with John's *Backed By Reality* AI × Bio essay.

**Status:** v1.1.0, data as of 13 Oct 2026. Repo **private** and site **behind Vercel login** until launch day (see BACKLOG.md § Launch). Read `docs/DECISIONS.md` before changing hosting, data model or the corrections route.

## Stack
- Static site: `index.html` + `methodology.html` + `assets/site.css`; reads `data/*.json` in the browser. No build step, no framework.
- Data master: `data/*.csv` (molecules, trials, candidates, excluded). JSON is generated.
- Python 3 scripts (stdlib, plus `markdown` for the methodology page).
- Corrections API: Vercel Node functions in `api/` (`corrections` POST, `corrections-log` GET, `admin` GET/PATCH), region lhr1 (`vercel.json`). One dependency, `@neondatabase/serverless`; pnpm 10 (`packageManager`), Node 22. Review page `admin.html` (Bearer `ADMIN_PASSWORD`).
- Hosting: Vercel project `ai-molecules-in-the-clinic` (team John M's projects), domain **aixbio-registry.org** (+ www). Deploys by CLI from the Mac clone, not on git push (no Git connection yet).
- Corrections queue: Neon Postgres, project `aixbio-registry` (`royal-tree-08432805`, aws-eu-west-2). Table `corrections`; public view `corrections_public`. App login `registry_web` (SELECT/INSERT/UPDATE on `corrections`, SELECT on the view; created in SQL because Neon API-created roles get superuser rights). Reached by Claude via the Neon MCP connector.

## Commands
| Task | Command |
|---|---|
| Rebuild JSON after any CSV edit | `python3 scripts/csv_to_json.py` |
| Refresh trials from ClinicalTrials.gov | `python3 scripts/fetch_trials.py` then `csv_to_json.py` |
| Rebuild methodology page after editing METHODOLOGY.md | `python3 scripts/build_site.py` |
| Preview locally | `python3 -m http.server 8765` |
| Deploy (from `~/Projects/ai-molecules-in-the-clinic` on the Mac) | `vercel deploy --prod --yes --scope john-ms-projects-7edbd1b5` |

`scripts/build_data.py` is a one-time v1.0.0 migration from the private workbook; do not rerun.

## Rules
- **CSV is the master.** Never hand-edit JSON or the HTML's numbers; every count on the site is computed from data.
- **Every data change is a logged release:** edit CSV → rebuild JSON → CHANGELOG line (date, evidence) → version bump in README, METHODOLOGY, index.html.
- **No count, inclusion or coding change without a source** and a check against METHODOLOGY.md. Corrections follow the same rule.
- **Personal data stays private.** Submitter names/emails live only in Neon `corrections`; nothing personal goes into the repo, the public view or the site.
- **Secrets** (Neon `DATABASE_URL`, Resend key, admin password) live in Vercel env only; `.env` locally, never committed. See `.env.example`.
- US English on the site; the site's voice is plain and factual.
- Git: commit as `220941196+JEM-Fizbit@users.noreply.github.com` (GitHub blocks the private email); remote uses the `github-personal` SSH alias.

## QA before deploy
Quick: JSON rebuilt; site loads with no console errors; headline numbers match README; screenshot desktop + 390px phone, light and dark. Full (data changes): spot-check changed rows against sources; recount strict/borderline totals.

## Protocol Triggers
- **ClinicalTrials.gov API (trial refresh, status checks)** → `docs/protocols/CLINICALTRIALS_GOV_API.md`
- **Before any deploy or release** → `docs/protocols/QA_PROTOCOL.md`
- **Backlog, promotion, specs** → `docs/protocols/ROADMAP_AND_BACKLOG.md`
- **Commits, runtime state** → `docs/protocols/GIT_CONVENTIONS.md`

## Key files
`README.md` · `METHODOLOGY.md` (definition and rules, public) · `CHANGELOG.md` · `CONTRIBUTING.md` · `docs/INCLUSION-FRAMEWORK.md` (v2.0 proposal, not adopted) · `docs/DECISIONS.md` · `BACKLOG.md`

## Gotchas
- A brand-new Vercel project's first CLI deploy goes straight to production. Protection is `ssoProtection: all` until launch; check a logged-out request returns 302 after any settings change.
- The Vercel MCP token cannot create projects, change settings or buy domains; use the `vercel` CLI on the Mac.
