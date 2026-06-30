from pathlib import Path
import shutil
import re
import yaml

ROOT = Path.cwd()
SOURCE = ROOT / "people"
OUTPUT = SOURCE / "generated"

GROUPS = ["faculty", "students", "alumni"]

def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")

if OUTPUT.exists():
    shutil.rmtree(OUTPUT)

for group in GROUPS:
    source_file = SOURCE / f"{group}.yml"

    if not source_file.exists():
        raise FileNotFoundError(f"Missing file: {source_file}")

    people = yaml.safe_load(source_file.read_text(encoding="utf-8"))

    if not isinstance(people, list):
        people = [people]

    out_dir = OUTPUT / group
    out_dir.mkdir(parents=True, exist_ok=True)

    for i, person in enumerate(people, start=1):
        filename = f"{i:02d}-{slugify(person['title'])}.yml"
        out_file = out_dir / filename

        with out_file.open("w", encoding="utf-8") as f:
            yaml.safe_dump(person, f, sort_keys=False, allow_unicode=True)

print("Generated people files.")
