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
physics_dominant = [m for m in S if re.search(r"Schr|Relay", m["developer"])]

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
    "minus_physics": len(S) - len(physics_dominant),
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
    ("METHODOLOGY.md", r"The strict count is about \*\*(\d+), −(\d+)/", [n["strict"], n["strict"] - n["minus_physics"]]),
    ("index.html", r"is about −(\d+) to \+8", [n["strict"] - n["minus_physics"]]),
    ("METHODOLOGY.md", r"excluding physics-dominant platforms gives \*\*(\d+)\*\*", [n["minus_physics"]]),
    ("METHODOLOGY.md", r"\| This registry \| (\d+) \|", [n["strict"]]),
    ("METHODOLOGY.md", r"(\d+) of (\d+) strict entries rest on", [n["not_a"], n["strict"]]),
]

bad = []
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
print(f"{len(checks) - len(bad)}/{len(checks)} counts match the data.")
sys.exit(1 if bad else 0)
