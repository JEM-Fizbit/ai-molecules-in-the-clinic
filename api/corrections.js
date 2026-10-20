// POST /api/corrections — public correction form. Stores the submission in Neon, then emails
// the maintainer and (if an address was given) acknowledges the submitter.
import { sql, send, readJson, clientIpHash, email } from "./_lib.js";

export const FIELDS = {
  inclusion: "Whether it should be counted",
  status: "Status (ongoing, stopped, unknown)",
  phase: "Furthest phase",
  target_type: "Target type",
  target_indication: "Target or indication",
  ai_role: "AI role or evidence for it",
  modality: "Modality",
  trials: "Trials or first dosing",
  sources: "Sources",
  new_entry: "A molecule that is missing",
  other: "Something else",
};

const clip = (v, n) => (v == null ? "" : String(v).trim().slice(0, n));
const EMAIL = /^[^\s@<>()",;]+@[^\s@<>()",;]+\.[a-z]{2,}$/i;
const HOURLY_LIMIT = 5;

export function validate(b) {
  const errors = {};
  const d = {
    molecule_id: clip(b.molecule_id, 80) || null,
    molecule_label: clip(b.molecule_label, 200),
    field: clip(b.field, 40),
    current_value: clip(b.current_value, 1000) || null,
    proposed_value: clip(b.proposed_value, 2000),
    source_url: clip(b.source_url, 500),
    notes: clip(b.notes, 2000) || null,
    submitter_name: clip(b.name, 120) || null,
    submitter_email: clip(b.email, 200) || null,
    affiliation: clip(b.affiliation, 200) || null,
    is_developer: b.is_developer === true || b.is_developer === "on" || b.is_developer === "true",
  };
  d.is_new_entry = d.field === "new_entry";
  if (!d.molecule_label) errors.molecule_label = "Name the molecule.";
  if (!FIELDS[d.field]) errors.field = "Choose what should change.";
  if (d.proposed_value.length < 3) errors.proposed_value = "Say what the entry should say.";
  try {
    const u = new URL(d.source_url);
    if (!/^https?:$/.test(u.protocol)) throw 0;
  } catch { errors.source_url = "Add a link to the source, starting with https://"; }
  if (d.submitter_email && !EMAIL.test(d.submitter_email)) errors.email = "That email address doesn't look complete.";
  return { data: d, errors };
}

export default async function handler(req, res) {
  if (req.method !== "POST") return send(res, 405, { error: "Use POST." }, { Allow: "POST" });
  let body;
  try { body = await readJson(req); } catch (e) { return send(res, e.status || 400, { error: e.message }); }

  // Bot traps: a hidden field people never fill, and a minimum time on the form.
  const tooFast = Number(body.elapsed_ms) > 0 && Number(body.elapsed_ms) < 3000;
  if (clip(body.website, 200) || tooFast) return send(res, 200, { ok: true, reference: "received" });

  const { data, errors } = validate(body);
  if (Object.keys(errors).length) return send(res, 422, { error: "Some fields need attention.", fields: errors });

  const ip_hash = clientIpHash(req);
  const db = sql();
  const [{ n }] = await db`SELECT count(*)::int AS n FROM corrections WHERE ip_hash = ${ip_hash} AND created_at > now() - interval '1 hour'`;
  if (n >= HOURLY_LIMIT) return send(res, 429, { error: "Too many submissions from this connection in the last hour. Try again later." });

  const [row] = await db`
    INSERT INTO corrections (molecule_id, molecule_label, is_new_entry, field, current_value, proposed_value, source_url, notes,
      submitter_name, submitter_email, affiliation, is_developer, ip_hash, user_agent)
    VALUES (${data.molecule_id}, ${data.molecule_label}, ${data.is_new_entry}, ${data.field}, ${data.current_value}, ${data.proposed_value},
      ${data.source_url}, ${data.notes}, ${data.submitter_name}, ${data.submitter_email}, ${data.affiliation}, ${data.is_developer},
      ${ip_hash}, ${clip(req.headers["user-agent"], 300) || null})
    RETURNING id, created_at`;
  const reference = row.id.slice(0, 8).toUpperCase();
  const site = process.env.SITE_URL || "https://aixbio-registry.org";

  const summary = [
    `Molecule: ${data.molecule_label}${data.molecule_id ? ` (${data.molecule_id})` : ""}`,
    `What should change: ${FIELDS[data.field]}`,
    data.current_value ? `Currently says: ${data.current_value}` : null,
    `Should say: ${data.proposed_value}`,
    `Source: ${data.source_url}`,
    data.notes ? `Notes: ${data.notes}` : null,
  ].filter(Boolean).join("\n");

  await Promise.all([
    email({
      to: process.env.CORRECTIONS_NOTIFY_TO,
      subject: `Registry correction ${reference}: ${data.molecule_label}`,
      text: `${summary}\n\nFrom: ${data.submitter_name || "(no name)"} <${data.submitter_email || "no email"}>${data.affiliation ? `, ${data.affiliation}` : ""}${data.is_developer ? " [says they work for the developer]" : ""}\n\nReview: ${site}/admin.html`,
      replyTo: data.submitter_email || undefined,
    }),
    data.submitter_email
      ? email({
          to: data.submitter_email,
          subject: `We received your correction (${reference})`,
          text: `Thank you for helping keep AI Molecules in the Clinic accurate.\n\nYour reference is ${reference}. We check every correction against its source and the registry's written rules. Decided corrections appear in the public log at ${site}/#corrections, without your name or email.\n\nWhat you sent:\n\n${summary}\n\nThis address does not receive replies. To add detail, send another correction quoting ${reference}.`,
        })
      : null,
  ]);

  return send(res, 201, { ok: true, reference });
}
