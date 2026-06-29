from pathlib import Path
import shutil
import yaml
import re

ROOT = Path(__file__).resolve().parents[1]

SOURCE = ROOT / "people"
OUTPUT = SOURCE / "generated"

FILES = [
    "faculty",
    "students",
    "alumni",
]


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


if OUTPUT.exists():
    shutil.rmtree(OUTPUT)

OUTPUT.mkdir(parents=True)

for group in FILES:

    people = yaml.safe_load((SOURCE / f"{group}.yml").read_text())

    out_dir = OUTPUT / group
    out_dir.mkdir(parents=True)

    for person in people:

        filename = slug(person["title"]) + ".yml"

        with open(out_dir / filename, "w") as f:
            yaml.safe_dump(
                person,
                f,
                sort_keys=False,
                allow_unicode=True,
            )

print("Generated people listing.")
