"""Check that every count written into README.md and METHODOLOGY.md matches data/*.csv.

The site computes its own numbers; these two files carry them as text, so they can drift.
Run after any data change (part of the QA gate). Exits 1 and lists mismatches if any.
"""
import csv, datetime, re, sys

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
NOVEL = [m for m in disclosed if m["target_precedence"] != "precedented"]
R = list(csv.DictReader(open("data/readouts.csv")))
with_trials = {i for t in T for i in t["molecule_ids"].split(";")}
physics_dominant = [m for m in S if re.search(r"Schr|Relay", m["developer"])]

n = {
    "strict": len(S),
    "borderline": len(B),
    "known": len(known),
    "disclosed": len(disclosed),
    "known_pct": f"{100 * len(known) / len(disclosed):.1f}%",
    "fic": sum(m["target_precedence"] == "first-in-class" for m in S),
    "novel": sum(m["target_precedence"] == "novel" for m in S),
    "rct_novel": len({r["molecule_id"] for r in R if r["randomized_efficacy"] == "yes"} & {m["id"] for m in NOVEL}),
    "nov": len(NOVEL),
    "nov_pct": f"{round(100 * len(NOVEL) / len(disclosed))}%",
    "p2_out": sum(rank(m["highest_phase"]) >= 4 or (rank(m["highest_phase"]) == 3 and m["status"] == "stopped") for m in S),
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
    ("README.md", r"\| Novel targets: tried in the clinic before / new to the clinic \| (\d+) / (\d+) \|", [n["novel"], n["fic"]]),
    ("README.md", r"\| Novel-target molecules with a randomized, placebo-controlled efficacy readout \| (\d+) \|", [n["rct_novel"]]),
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
    ("METHODOLOGY.md", r"excluding the remaining physics-dominant platform entries gives \*\*(\d+)\*\*", [n["minus_physics"]]),
    ("METHODOLOGY.md", r"\| This registry \| (\d+) \|", [n["strict"]]),
    ("METHODOLOGY.md", r"(\d+) of (\d+) strict entries rest on", [n["not_a"], n["strict"]]),
    # Static text the site shows before its script runs, and in link previews (og:description).
    ("index.html", r'og:description" content="(\d+) AI-derived molecules have been dosed in people\. (None is|One is|\d+ are) approved', [n["strict"], {0: "None is", 1: "One is"}.get(n["approved"], f'{n["approved"]} are')]),
    ("index.html", r'<span id="h-n">(\d+)</span>', [n["strict"]]),
    ("index.html", r'<span id="h-appr">(None is|One is|\d+ are) approved', [{0: "None is", 1: "One is"}.get(n["approved"], f'{n["approved"]} are')]),
    ("index.html", r'<span id="h-most">([^<]+)</span>', ["Most" if 2 * n["known"] > n["disclosed"] else "Half" if 2 * n["known"] == n["disclosed"] else "Fewer than half"]),
    ("index.html", r'<span id="h-known">(\d+)</span> of the <span id="h-disc">(\d+)</span>', [n["known"], n["disclosed"]]),
    ("index.html", r'<span id="h-nov">(\d+)</span> \(<span id="h-nov-pct">(\d+%)</span>\).*?<span id="h-nov-tried">(\d+)</span>.*?<span id="h-nov-new">(\d+)</span>', [n["nov"], n["nov_pct"], n["novel"], n["fic"]]),
    ("index.html", r'Of those (\d+), (\w+) \(', [n["nov"], WORDS[n["rct_novel"]]]),
    ("index.html", r'<span id="h-p2">Only (\d+) have', [n["p2_out"]]),
    ("index.html", r'<span id="n-self">(\d+)</span>', [n["not_a"]]),
    ("question.html", r'<span data-n="strict">(\d+)</span>', [n["strict"]]),
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

# Readout watch: a Phase 2+ trial of a novel-target molecule whose primary completion date has
# passed needs a row in readouts.csv (a readout, or "no" with the date checked); "no" rows expire
# after 180 days. Keeps "N on novel targets have a randomized readout" from going stale.
today = datetime.date.today().isoformat()
stale = (datetime.date.today() - datetime.timedelta(days=180)).isoformat()
logged = {r["trial_id"]: r for r in R}
for t in T:
    if t["phase"] in ("Phase 2", "Phase 2/Phase 3", "Phase 3") and set(t["molecule_ids"].split(";")) & {m["id"] for m in NOVEL} \
            and t["primary_completion_date"] and t["primary_completion_date"] < today:
        r = logged.get(t["nct_id"])
        if not r or (r["randomized_efficacy"] == "no" and r["readout_date"] < stale):
            bad.append(f"readouts.csv: {t['nct_id']} ({t['molecule_ids']}) passed primary completion {t['primary_completion_date']}; "
                       "look for a readout and record it, or record 'no' with today's date")

for b in bad: print("MISMATCH", b)
print(f"{len(checks) - len(bad)}/{len(checks)} counts match the data.")
sys.exit(1 if bad else 0)
