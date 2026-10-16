"""One-time migration (v1.0.0): built data/ from the maintainer's private working file.

From v1.0.0 on, data/*.csv are the master. Edit them directly (via a reviewed correction)
and run scripts/csv_to_json.py; refresh trials with scripts/fetch_trials.py.
"""
import csv, json, re, sys, unicodedata
import openpyxl

wb_path, trials_path = sys.argv[1], sys.argv[2]
AS_OF = "2026-10-13"
wb = openpyxl.load_workbook(wb_path, read_only=True)

def rows(sheet):
    r = list(wb[sheet].iter_rows(values_only=True))
    h = [c for c in r[0]]
    return [dict(zip(h, x)) for x in r[1:] if any(x)]

def slug(name):
    first = re.split(r"\s*/\s*|\s*\(", name)[0].strip()
    s = unicodedata.normalize("NFKD", first).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

REG = re.compile(r"\b(NCT\d{8}|ACTRN\d{14}|CTR\d{8}|jRCT\d{10}|ChiCTR\d+|EUCT[\d-]+)\b")
def reg_ids(d):
    txt = " ".join(str(v) for v in d.values() if v)
    return sorted(set(REG.findall(txt)))

def year(s):
    m = re.search(r"(19|20)\d{2}", str(s or ""))
    return int(m.group(0)) if m else None

def clean(v):
    return re.sub(r"\s+", " ", str(v)).strip() if v not in (None, "") else ""

FIELDS = ["id","molecule","developer","partner","modality","target","indication","inclusion","inclusion_note",
          "ai_role","attribution_tier","first_in_human_year","first_in_human_detail","highest_phase","status",
          "status_detail","target_precedence","precedence_basis","confidence","registry_ids","sources","notes","as_of"]

def to_rec(d, inclusion, note_field="notes"):
    rec = {
        "molecule": clean(d.get("molecule")), "developer": clean(d.get("company")), "partner": clean(d.get("partner")) if clean(d.get("partner")).lower() not in ("none","n/a") else "",
        "modality": clean(d.get("modality")), "target": clean(d.get("target")), "indication": clean(d.get("indication")),
        "inclusion": inclusion, "inclusion_note": clean(d.get("notes")) if inclusion != "strict" else "",
        "ai_role": clean(d.get("ai_role")), "attribution_tier": clean(d.get("ai_attribution_tier")),
        "first_in_human_year": year(d.get("first_in_human")), "first_in_human_detail": clean(d.get("first_in_human")),
        "highest_phase": clean(d.get("highest_phase")), "status": clean(d.get("status_class")), "status_detail": clean(d.get("status_now")),
        "target_precedence": clean(d.get("target_precedence")), "precedence_basis": clean(d.get("precedence_basis")),
        "confidence": clean(d.get("confidence")), "registry_ids": ";".join(reg_ids(d)),
        "sources": ";".join(u.strip() for u in re.split(r"[\n;]+| ; ", str(d.get("sources") or "")) if u.strip().startswith("http")),
        "notes": "; ".join(x for x in [clean(d.get("notes")) if inclusion == "strict" else "", clean(d.get("verifier_note"))] if x),
        "as_of": AS_OF,
    }
    rec["id"] = slug(rec["molecule"])
    return rec

mols = [to_rec(d, "strict") for d in rows("Strict cohort")] + [to_rec(d, "borderline") for d in rows("Borderline")]
ids = [m["id"] for m in mols]
dups = {i for i in ids if ids.count(i) > 1}
assert not dups, dups
cands = [to_rec(d, "candidate") for d in rows("Unverified candidates")]
excl = [{"molecule": clean(d["molecule"]), "reason": clean(d["reason"]), "as_of": AS_OF} for d in rows("Excluded")]

def write(path, recs, fields):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(recs)

write("data/molecules.csv", mols, FIELDS)
write("data/candidates.csv", cands, FIELDS)
write("data/excluded.csv", excl, ["molecule","reason","as_of"])
json.dump({"as_of": AS_OF, "molecules": mols}, open("data/molecules.json", "w"), indent=1, ensure_ascii=False)

# trials: ClinicalTrials.gov records for strict-cohort molecules
name2id = {}
for m in mols:
    name2id[m["molecule"]] = m["id"]
tr = json.load(open(trials_path))
trials = []
for t in tr.values():
    mid = ";".join(sorted({name2id.get(x, slug(x)) for x in t.get("molecules", [])}))
    trials.append({"nct_id": t["nct"], "molecule_ids": mid, "title": clean(t.get("title")), "phase": "/".join(p.replace("PHASE","Phase ").replace("EARLY_","Early ") for p in t.get("phases", [])),
                   "status": t.get("status") or "", "start_date": t.get("start") or "", "primary_completion_date": t.get("pcd") or "",
                   "primary_completion_type": t.get("pcd_type") or "", "lead_sponsor": t.get("sponsor") or "", "sponsor_class": t.get("sponsor_class") or "",
                   "why_stopped": clean(t.get("why")), "retrieved": "2026-10-15"})
trials.sort(key=lambda x: (x["molecule_ids"], x["start_date"]))
write("data/trials.csv", trials, list(trials[0].keys()))
json.dump({"retrieved": "2026-10-15", "trials": trials}, open("data/trials.json", "w"), indent=1, ensure_ascii=False)

s = [m for m in mols if m["inclusion"] == "strict"]
from collections import Counter
print(len(s), "strict;", len(mols) - len(s), "borderline;", len(cands), "candidates;", len(excl), "excluded;", len(trials), "trials")
print(Counter(m["target_precedence"] for m in s)); print(Counter(m["status"] for m in s)); print(Counter(m["attribution_tier"] for m in s))
unmatched = [t["nct_id"] for t in trials if not any(i in ids for i in t["molecule_ids"].split(";"))]
print("trials with unmatched molecule ids:", unmatched)
