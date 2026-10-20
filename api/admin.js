// /api/admin — maintainer review queue. Bearer ADMIN_PASSWORD.
// GET ?status=received → submissions; PATCH { id, status, assessment, decision_reason, released_in } → update one.
import { sql, send, readJson, isAdmin } from "./_lib.js";

const STATUSES = ["received", "checking", "accepted", "declined", "released", "spam"];
const DECIDED = new Set(["accepted", "declined", "released"]);

export default async function handler(req, res) {
  const noStore = { "Cache-Control": "no-store" };
  if (!isAdmin(req)) return send(res, 401, { error: "Wrong or missing password." }, noStore);
  const db = sql();

  if (req.method === "GET") {
    const url = new URL(req.url, "http://x");
    const status = url.searchParams.get("status");
    const rows = status && STATUSES.includes(status)
      ? await db`SELECT * FROM corrections WHERE status = ${status} ORDER BY created_at DESC LIMIT 500`
      : await db`SELECT * FROM corrections ORDER BY created_at DESC LIMIT 500`;
    const counts = await db`SELECT status, count(*)::int AS n FROM corrections GROUP BY status`;
    return send(res, 200, { corrections: rows.map(({ ip_hash, user_agent, ...r }) => r), counts }, noStore);
  }

  if (req.method === "PATCH") {
    let b;
    try { b = await readJson(req); } catch (e) { return send(res, e.status || 400, { error: e.message }, noStore); }
    if (!b.id || !STATUSES.includes(b.status)) return send(res, 422, { error: "Need an id and a valid status." }, noStore);
    const [row] = await db`
      UPDATE corrections SET
        status = ${b.status},
        assessment = ${b.assessment ?? null},
        decision_reason = ${b.decision_reason ?? null},
        released_in = ${b.released_in ?? null},
        decided_at = CASE WHEN ${DECIDED.has(b.status)} THEN coalesce(decided_at, now()) ELSE NULL END
      WHERE id = ${b.id}
      RETURNING id, status, decided_at`;
    if (!row) return send(res, 404, { error: "No such correction." }, noStore);
    return send(res, 200, { ok: true, correction: row }, noStore);
  }

  return send(res, 405, { error: "Use GET or PATCH." }, { Allow: "GET, PATCH", ...noStore });
}
