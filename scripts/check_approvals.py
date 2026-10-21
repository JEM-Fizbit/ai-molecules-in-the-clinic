"""Look for FDA approvals the registry has not recorded (Drugs@FDA via openFDA).

Trial registries do not record approvals, so a molecule can be approved while its row still
reads "Phase 2" (lirafugratinib, October 2026). Run before each release and each refresh.
Searches every alias of every Phase 2+ entry as an active ingredient and brand name; prints
approvals that are missing from the `approvals` column. Exits 1 if any are found.
Non-US regulators (EMA, NMPA, PMDA) still need a manual check; see the refresh checklist.
"""
import csv, json, re, sys, time, urllib.error, urllib.parse, urllib.request

API = "https://api.fda.gov/drug/drugsfda.json"

def search(term):
    q = f'products.active_ingredients.name:"{term}"+products.brand_name:"{term}"'
    try:
        with urllib.request.urlopen(f"{API}?search={urllib.parse.quote(q, safe='+:')}&limit=100", timeout=30) as r:
            return json.load(r).get("results", [])
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return []
        raise

def rank(p):
    return 3 if re.search(r"Phase (2|3)|Approved", p) and not p.startswith("Phase 1") else 1

missing = []
rows = [m for m in csv.DictReader(open("data/molecules.csv")) if rank(m["highest_phase"]) >= 3]
for m in rows:
    recorded = set(re.findall(r"(?:NDA|BLA|ANDA) ?(\d{6})", m.get("approvals", "")))
    # Once an approval is recorded, another sponsor's product of the same ingredient (e.g. a
    # dexmedetomidine injection against BXCL-501) is not this molecule; flag only our sponsors'.
    ours = {w for w in re.findall(r"[a-z]{4,}", (m["developer"] + " " + m["partner"]).lower())} - {"therapeutics", "pharma", "pharmaceuticals", "medicine", "biosciences", "limited", "corporation"}
    # Names only: skip internal codes, which Drugs@FDA does not index.
    names = {a.strip().split(" (")[0] for a in m["molecule"].split("/")}
    names = {n for n in names if re.fullmatch(r"[A-Za-z][a-z]{4,}", n)}
    for n in sorted(names):
        for app in search(n.upper()):
            num = re.sub(r"\D", "", app["application_number"])
            if app["application_number"].startswith("ANDA"):
                continue  # generics of an already-approved drug
            if recorded and not ours & set(re.findall(r"[a-z]{4,}", app.get("sponsor_name", "").lower())):
                continue
            if any(s.get("submission_status") == "AP" for s in app.get("submissions", [])) and num not in recorded:
                missing.append(f"{m['id']}: {app['application_number']} ({app.get('sponsor_name')}) matches '{n}' but is not in `approvals`")
        time.sleep(0.3)

for x in missing: print("UNRECORDED", x)
print(f"Checked {len(rows)} Phase 2+ entries against Drugs@FDA; {len(missing)} unrecorded approvals.")
sys.exit(1 if missing else 0)
