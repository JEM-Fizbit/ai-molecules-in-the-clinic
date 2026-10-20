"""Refresh data/trials.csv from ClinicalTrials.gov (API v2) for strict-cohort molecules.

Matches by NCT numbers in molecules.csv `registry_ids` plus an intervention-name search on each
alias (name match verified against intervention names and titles). Then run csv_to_json.py.
"""
import csv, json, re, time, urllib.parse, urllib.request
from datetime import date

API = "https://clinicaltrials.gov/api/v2/studies"
norm = lambda x: re.sub(r"[^a-z0-9]", "", (x or "").lower())

def get(params):
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            return json.load(urllib.request.urlopen(url, timeout=60))
        except Exception:
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(url)

def flat(s):
    p = s["protocolSection"]; st = p["statusModule"]; arms = p.get("armsInterventionsModule", {}).get("interventions", [])
    names = [i.get("name") for i in arms] + sum([i.get("otherNames", []) for i in arms], [])
    sp = p.get("sponsorCollaboratorsModule", {}).get("leadSponsor", {})
    return {"nct_id": p["identificationModule"]["nctId"], "title": p["identificationModule"].get("briefTitle", ""),
            "phase": "/".join(x.replace("PHASE", "Phase ").replace("EARLY_", "Early ") for x in p.get("designModule", {}).get("phases", [])),
            "status": st.get("overallStatus", ""), "start_date": st.get("startDateStruct", {}).get("date", ""),
            "primary_completion_date": st.get("primaryCompletionDateStruct", {}).get("date", ""),
            "primary_completion_type": st.get("primaryCompletionDateStruct", {}).get("type", ""),
            "lead_sponsor": sp.get("name", ""), "sponsor_class": sp.get("class", ""), "why_stopped": st.get("whyStopped", ""),
            "_names": names}

mols = [m for m in csv.DictReader(open("data/molecules.csv")) if m["inclusion"] == "strict"]
found = {}
for m in mols:
    aliases = [a.strip() for a in re.split(r"[/()]", m["molecule"]) if len(norm(a)) >= 4]
    ids = {i for i in m["registry_ids"].split(";") if i.startswith("NCT")}
    for a in aliases:
        for s in get({"query.intr": a, "pageSize": 50}).get("studies", []):
            f = flat(s)
            if any(norm(a) in norm(n) for n in f["_names"]) or norm(a) in norm(f["title"]):
                ids.add(f["nct_id"]); found[f["nct_id"]] = f
    for n in ids - set(found):
        for s in get({"query.term": n, "pageSize": 5}).get("studies", []):
            f = flat(s)
            if f["nct_id"] == n: found[n] = f
    for n in ids:
        if n in found: found[n].setdefault("_mols", set()).add(m["id"])

today = date.today().isoformat()
rows = []
for f in found.values():
    if not f.get("_mols"): continue
    r = {k: v for k, v in f.items() if not k.startswith("_")}
    r["molecule_ids"] = ";".join(sorted(f["_mols"])); r["retrieved"] = today
    rows.append(r)
fields = ["nct_id","molecule_ids","title","phase","status","start_date","primary_completion_date","primary_completion_type","lead_sponsor","sponsor_class","why_stopped","retrieved"]
rows.sort(key=lambda x: (x["molecule_ids"], x["start_date"]))
with open("data/trials.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=fields); w.writeheader(); w.writerows(rows)
print(len(rows), "trials for", len({i for r in rows for i in r["molecule_ids"].split(";")}), "molecules")
