# Working Decisions Log

> Locked design decisions, with rationale. Append-only: a reversal is a new entry citing the old one. Newest first.

---

## 2026-10-20 — Evidence-first re-review of every entry; stricter attribution test; headline gate

**Decision:**
- **Scope:** re-review every entry, strict, borderline and excluded, under a protocol written before the review starts. It is piloted on a calibration set with known answers and cross-validated against other published lists (Jayatunga 2024, Greenblatt & Geoui 2026, Wellcome 2023). John signs off each strict entry.
- **Stricter test:** a strict entry needs a verbatim claim, by the developer or a partner, that AI or ML chose the target or designed *this* molecule, and the claim must say what the AI did. Platform-level language alone, or "developed using our AI platform", is borderline.
- **Headline gate:** a change to a headline number (strict count, approvals, first-in-class) needs the acid test plus sources, and waits 24 hours before deploy.
- **The essay:** its figures are held until the re-review is signed off.

**Why:** lirafugratinib was counted as the first approved AI drug (v1.1.14–v1.1.17) on a platform-level claim, while its own developer, licensee and the field made no such claim. Strict fell from 55 to 49 in a day as § 1.2 was applied literally. Earlier checks verified that sources existed and that quotes matched them, not that the evidence met the rule, and AI agents built and audited the registry with no human sign-off.

**Supersedes:** the lenient reading of § 1.2 used in the 13 October 2026 build.

---

## 2026-10-20 — Approvals recorded against the regulator's record; IND clearances not tracked

**Decision:** Add an `approvals` column to `molecules.csv`. Each entry gives the agency, date, reference, indication and a link to the regulator's own record, such as a Drugs@FDA application page. `scripts/check_counts.py` fails if an approved row has no entry. Trials also record protocol and analysis-plan PDFs posted on ClinicalTrials.gov. IND clearances are not tracked as a field.

**Why:** An approval is the strongest claim the registry can make, so it should trace to the regulator, not to a press release. The lirafugratinib approval was missed because checks looked at trial registries, which do not record approvals. US INDs are confidential, so FDA publishes no IND list; clearances are known only from sponsor announcements. A field would therefore be selective and could not be verified for most rows. Dosing, the inclusion test, is what registries record. FDA does not approve protocols; it reviews them under an IND.

**Revisit:** a pre-clinic watchlist of announced IND or CTA clearances, including China CDE's public implied-approval list, could be a separate list after launch.

---

## 2026-10-20 — Per-row verification date and a field-level audit log

**Decision:** Every row in `molecules.csv`, `candidates.csv` and `excluded.csv` carries a `last_verified` ISO date: the day each of its fields was last checked against primary sources. `data/audit-log.csv` records the evidence, one line per row and field: `id, field, verdict (confirmed/changed/flagged), old_value, new_value, source_url, quote, checked_date`. Quotes are verbatim and 25 words or fewer. The log is append-only; a later check adds lines rather than editing old ones. `excluded.csv` gains a stable `id` column (prefix `x-`) so its rows can be referenced in the log. The site shows "Last verified" in each entry's expanded view and links the log.

**Why:** CEL383 was renamed ABBV-8736 after AbbVie bought Celsius, and the row stayed stale until 20 Oct. `as_of` says when the data was cut, not when a row was last checked, and per-source spot checks left no trail. A dated, quoted log per field lets a reader or second coder see exactly what each value rests on, and shows which rows are due for a recheck.

**Alternatives rejected:** a per-field date column for each field (doubles the CSV width); evidence in `notes` (mixes reader text with process); a log in the private Neon database (the evidence should be as open as the data).

---

## 2026-10-20 — Public ahead of the essay

**Decision:** The registry went public on 20 Oct 2026 at 09:15, before the essay. The GitHub repo is public. Vercel `ssoProtection` is back to `all_except_custom_domains`. The `claude-smoke-test` bypass token is revoked.

**Why:** John's call. The data, corrections route and site were ready, so there was no reason to hold them for the essay date.

**Supersedes:** the "behind login until launch day" part of the 19 Oct entry "Launch on v1 with the essay". The essay launch still triggers a trial re-pull and a release note (BACKLOG.md § Essay launch day).

---

## 2026-10-20 — Emailed corrections go into the same queue

**Decision:** `corrections@aixbio-registry.org` will receive mail through Resend Receiving, with an inbound webhook that files each email into Neon `corrections` alongside form submissions.

**Why:** Some people prefer email, and acknowledgements invite replies; one queue keeps one review page, one reference scheme and one public log, with no inbox to watch.

**Alternatives rejected:** forwarding to John's inbox (two places to look, manual re-keying, another forwarding service since Vercel has none); send-only address (replies lost).

## 2026-10-19 — Corrections via a webform into Neon, not GitHub issues

**Decision:** Corrections come in through a form on the site, stored in a private Neon Postgres table (`corrections`, aws-eu-west-2). Resend emails John on each submission and acknowledges the submitter. Decided items appear in a public "Corrections log" via the `corrections_public` view (no personal data). GitHub issues stay open as an optional route.

**Why:** Many readers (pharma, biotech, investors) have no GitHub account. A private store keeps submitter contact details out of public view; the public log keeps the correction trail visible, which is part of the registry's credibility. The official Neon MCP connector lets Claude read and annotate the queue directly, unattended.

**Alternatives rejected:** GitHub issues only (account barrier, public personal data). Inbox as queue via Iris (public address on an agent-actioned inbox; needs the inbox for state). insight-ca.com mailbox (reachable only via the Mac; plan has no extra mailboxes). Supabase (≈$10/mo for a new project; free tier pauses after a week idle). Vercel marketplace Neon (Vercel-managed account the connector cannot see).

**Related:** chat with John, 19 Oct 2026. Not yet built: see BACKLOG.md.

---

## 2026-10-19 — Domain aixbio-registry.org

**Decision:** Registered `aixbio-registry.org` (Vercel registrar, $9.99, auto-renew) to Insight Capital & Advisory Ltd at its registered office; attached apex + www to the Vercel project.

**Why:** A readable, durable address ahead of launch; John chose the AIxBio framing (the bare aixbio .com/.org/.net were taken). Company registered office keeps John's home address out of registration records.

**Alternatives rejected:** aimolecules.org, aixbioregistry.org (John preferred the hyphenated form), aixbio.io ($46/yr renewal).

---

## 2026-10-19 — Launch on v1 with the essay; host on Vercel behind login until then

**Decision:** Publish v1.x (current definition) with the essay; harden v1 meanwhile. Static site on Vercel with Vercel Authentication on all deployments, including production, until launch day.

**Why:** The essay's figures are v1's; the corrections process answers the single-coder limitation. The v2.0 inclusion framework (`docs/INCLUSION-FRAMEWORK.md`) would move the headline count after publication if rushed.

**Alternatives rejected:** wait for v2.0; GitHub Pages (requires a public repo before launch).
