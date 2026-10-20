// GET /api/corrections-log — public list of decided corrections. No personal data: reads the
// corrections_public view, which excludes submitter details, notes and anything undecided.
import { sql, send } from "./_lib.js";

export default async function handler(req, res) {
  if (req.method !== "GET") return send(res, 405, { error: "Use GET." }, { Allow: "GET" });
  const rows = await sql()`
    SELECT id, created_at, molecule_label, is_new_entry, field, proposed_value, source_url, status, decision_reason, decided_at, released_in
    FROM corrections_public ORDER BY decided_at DESC NULLS LAST, created_at DESC LIMIT 500`;
  return send(res, 200, {
    corrections: rows.map(r => ({ ...r, reference: r.id.slice(0, 8).toUpperCase(), id: undefined })),
  }, { "Cache-Control": "public, s-maxage=300, stale-while-revalidate=600" });
}
