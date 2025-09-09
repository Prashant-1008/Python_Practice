from pathlib import Path
import csv
import json


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    csv_path = Path("people.csv")
    json_path = Path("people.json")
    people = [
        {"name": "Alice", "city": "Pune"},
        {"name": "Bob", "city": "Mumbai"},
    ]
    write_csv(csv_path, people)
    print(read_csv(csv_path))
    write_json(json_path, people)
    print(read_json(json_path)) 