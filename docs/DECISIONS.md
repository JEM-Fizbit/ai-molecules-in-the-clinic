# Working Decisions Log

> Locked design decisions, with rationale. Append-only: a reversal is a new entry citing the old one. Newest first.

---

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
