"""Check that every count written into README.md and METHODOLOGY.md matches data/*.csv.

The site computes its own numbers; these two files carry them as text, so they can drift.
Run after any data change (part of the QA gate). Exits 1 and lists mismatches if any.
"""
import csv, re, sys

M = list(csv.DictReader(open("data/molecules.csv")))
T = list(csv.DictReader(open("data/trials.csv")))
S = [m for m in M if m["inclusion"] == "strict"]
B = [m for m in M if m["inclusion"] == "borderline"]

def rank(p):
    if re.search(r"Approved", p, re.I): return 5
    if "Phase 3" in p: return 4
    if re.search(r"Phase 2 \(of", p): return 3
    if "Phase 1/2" in p: return 2
    if "Phase 2" in p: return 3
    return 1

disclosed = [m for m in S if m["target_precedence"] != "unclear"]
known = [m for m in disclosed if m["target_precedence"] == "precedented"]
with_trials = {i for t in T for i in t["molecule_ids"].split(";")}

n = {
    "strict": len(S),
    "borderline": len(B),
    "known": len(known),
    "disclosed": len(disclosed),
    "known_pct": f"{100 * len(known) / len(disclosed):.1f}%",
    "fic": sum(m["target_precedence"] == "first-in-class" for m in S),
    "ph2plus": sum(rank(m["highest_phase"]) >= 3 for m in S),
    "ph3": sum(rank(m["highest_phase"]) == 4 for m in S),
    "approved": sum(rank(m["highest_phase"]) == 5 for m in S),
    "stopped": sum(m["status"] == "stopped" for m in S),
    "tier_a": sum(m["attribution_tier"] == "A" for m in S),
    "not_a": sum(m["attribution_tier"] != "A" for m in S),
    "trials": len(T),
    "trial_mols": len({i for t in T for i in t["molecule_ids"].split(";")}),
    "no_ctgov": sum(m["id"] not in with_trials for m in S),
    "plus_physics": len(S) + sum(m["borderline_reason"] == "physics_only" for m in B),
    "n_physics": sum(m["borderline_reason"] == "physics_only" for m in B),
    "plus_platform": len(S) + sum(m["borderline_reason"] == "platform_only" for m in B),
    "n_platform": sum(m["borderline_reason"] == "platform_only" for m in B),
}
WORDS = "zero one two three four five six seven eight nine ten eleven twelve".split()

checks = [  # (file, regex with one group per expected value, expected values)
    ("README.md", r"\| Strict cohort \| \*\*(\d+)\*\* molecules \|", [n["strict"]]),
    ("README.md", r"\| Known \(precedented\) targets, of (\d+) disclosed \| (\d+) \(([\d.]+%)\) \|", [n["disclosed"], n["known"], n["known_pct"]]),
    ("README.md", r"\| First-in-class targets \| (\d+) \|", [n["fic"]]),
    ("README.md", r"\| Reached Phase 2 or later / now in Phase 3 \| (\d+) / (\d+) \|", [n["ph2plus"], n["ph3"]]),
    ("README.md", r"\| Approved \| (\d+)\b", [n["approved"]]),
    ("README.md", r"\| Stopped \(discontinued, terminated, deprioritised\) \| (\d+) \|", [n["stopped"]]),
    ("README.md", r"\| AI role documented beyond the developer's own word \| (\d+) of (\d+) \|", [n["tier_a"], n["strict"]]),
    ("README.md", r"\| Borderline entries \(published, not counted\) \| (\d+) \|", [n["borderline"]]),
    ("README.md", r"\((\d+) trials, (\d+) molecules\)", [n["trials"], n["trial_mols"]]),
    ("README.md", r"(\d+) of the (\d+) strict entries rest on", [n["not_a"], n["strict"]]),
    ("METHODOLOGY.md", r"(\w+) strict molecules have no ClinicalTrials\.gov record", [WORDS[n["no_ctgov"]].capitalize()]),
    ("METHODOLOGY.md", r"The strict count is about \*\*(\d+), −2/\+8\*\*", [n["strict"]]),
    ("METHODOLOGY.md", r"counting physics-based design gives \*\*(\d+)\*\*: adding the (\d+) borderline", [n["plus_physics"], n["n_physics"]]),
    ("METHODOLOGY.md", r"counting platform-level attribution gives \*\*(\d+)\*\*: adding the (\d+) borderline", [n["plus_platform"], n["n_platform"]]),
    ("METHODOLOGY.md", r"\| This registry \| (\d+) \|", [n["strict"]]),
    ("METHODOLOGY.md", r"(\d+) of (\d+) strict entries rest on", [n["not_a"], n["strict"]]),
]

# The ladder (METHODOLOGY § 5): cumulative counts by rung, and where each published list's entries fall.
RUNGS = [
    ("Strict, AI step stated", lambda m: m["inclusion"] == "strict" and m.get("ai_step_stated") == "yes"),
    ("Strict", lambda m: m["inclusion"] == "strict"),
    ("+ platform-only", lambda m: m["borderline_reason"] == "platform_only"),
    ("+ physics-based", lambda m: m["borderline_reason"] == "physics_only"),
    ("+ repurposing, vaccines, other", lambda m: m["inclusion"] == "borderline"),
]
def rung(m):
    for i, (_, f) in enumerate(RUNGS):
        if m and f(m): return i
    return 99
BYID = {m["id"]: m for m in M}
XW = list(csv.DictReader(open("data/crosswalk.csv")))
LISTS = ["jayatunga2024", "greenblatt2026", "wellcome2023", "mckinsey2026"]
per = {k: [rung(BYID.get(r["registry_id"])) for r in XW if r["source"] == k] for k in LISTS}
ladder_checks = []
for i, (label, _) in enumerate(RUNGS):
    want = [sum(rung(m) <= i for m in M)] + [sum(x <= i for x in per[k]) for k in LISTS]
    ladder_checks.append(("METHODOLOGY.md", r"\| " + re.escape(label) + r" \| \*\*(\d+)\*\* \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|", want))
ladder_checks.append(("METHODOLOGY.md", r"\| Excluded here, or not in this registry \| – \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|", [sum(x == 99 for x in per[k]) for k in LISTS]))
checks += ladder_checks
pre = [f"molecules.csv: strict row {m['id']} has no ai_step_stated yes/no" for m in S if m.get("ai_step_stated") not in ("yes", "no")]

bad = list(pre)
# Every approved row must cite its approval record (agency|date|reference|indication|url).
for m in M:
    if re.match(r"Approved", m["highest_phase"], re.I) and not m.get("approvals"):
        bad.append(f"molecules.csv: {m['id']} is approved but has no `approvals` entry")
for f, rx, want in checks:
    m = re.search(rx, open(f).read())
    if not m:
        bad.append(f"{f}: pattern not found: {rx}")
        continue
    got = list(m.groups())
    if [str(w) for w in want] != got:
        bad.append(f"{f}: {rx}\n    text says {got}, data says {want}")

for b in bad: print("MISMATCH", b)
print(f"{len(checks) - len(bad) + len(pre)}/{len(checks)} counts match the data." + (f" {len(pre)} strict rows lack ai_step_stated." if pre else ""))
sys.exit(1 if bad else 0)
