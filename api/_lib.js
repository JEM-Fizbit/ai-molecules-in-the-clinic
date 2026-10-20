// Shared helpers for the corrections API. Files starting with "_" are not routes on Vercel.
import { neon } from "@neondatabase/serverless";
import { createHash, timingSafeEqual } from "node:crypto";

let _sql;
export function sql() {
  if (!process.env.DATABASE_URL) throw new Error("DATABASE_URL is not set");
  _sql ??= neon(process.env.DATABASE_URL);
  return _sql;
}

export function send(res, status, body, headers = {}) {
  res.statusCode = status;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("X-Content-Type-Options", "nosniff");
  for (const [k, v] of Object.entries(headers)) res.setHeader(k, v);
  res.end(JSON.stringify(body));
}

export async function readJson(req, limit = 20_000) {
  if (req.body && typeof req.body === "object") return req.body;
  let raw = "";
  for await (const chunk of req) {
    raw += chunk;
    if (raw.length > limit) throw Object.assign(new Error("Request too large"), { status: 413 });
  }
  try { return JSON.parse(raw || "{}"); } catch { throw Object.assign(new Error("Request body is not valid JSON"), { status: 400 }); }
}

export function clientIpHash(req) {
  const ip = String(req.headers["x-forwarded-for"] || "").split(",")[0].trim() || req.socket?.remoteAddress || "unknown";
  return createHash("sha256").update(ip + (process.env.IP_HASH_SALT || "")).digest("hex").slice(0, 32);
}

export function isAdmin(req) {
  const want = process.env.ADMIN_PASSWORD || "";
  const got = String(req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  if (!want || want.length < 12) return false;
  const a = Buffer.from(want), b = Buffer.from(got);
  return a.length === b.length && timingSafeEqual(a, b);
}

// Best-effort email through Resend. Never throws: a failed email must not lose a submission.
export async function email({ to, subject, text, replyTo }) {
  const key = process.env.RESEND_API_KEY, from = process.env.CORRECTIONS_FROM;
  if (!key || !from || !to) return { sent: false, reason: "email not configured" };
  try {
    const r = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
      body: JSON.stringify({ from, to: [to], subject, text, ...(replyTo ? { reply_to: replyTo } : {}) }),
      signal: AbortSignal.timeout(5000),
    });
    return { sent: r.ok, status: r.status };
  } catch (e) {
    return { sent: false, reason: e.name };
  }
}
