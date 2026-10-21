"""Regenerate data/*.json from the master CSVs. Run after any edit to data/*.csv."""
import csv, json
mols = list(csv.DictReader(open("data/molecules.csv")))
for m in mols:
    m["first_in_human_year"] = int(m["first_in_human_year"]) if m["first_in_human_year"] else None
as_of = max(m["as_of"] for m in mols)
readouts = list(csv.DictReader(open("data/readouts.csv")))
json.dump({"as_of": as_of, "molecules": mols, "readouts": readouts}, open("data/molecules.json", "w"), indent=1, ensure_ascii=False)
trials = list(csv.DictReader(open("data/trials.csv")))
json.dump({"retrieved": max(t["retrieved"] for t in trials), "trials": trials}, open("data/trials.json", "w"), indent=1, ensure_ascii=False)
print(len(mols), "molecules,", len(trials), "trials")
