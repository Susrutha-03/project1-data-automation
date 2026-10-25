
import csv
import json
from pathlib import Path


def read_csv(file_path):
    """Read records from a CSV file."""
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    with path.open(
        mode="r",
        newline="",
        encoding="utf-8-sig"
    ) as file:
        return list(csv.DictReader(file))


def read_json(file_path):
    """Read records from a JSON file."""
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    with path.open("r", encoding="utf-8-sig") as file:
        records = json.load(file)

    if not isinstance(records, list):
        raise ValueError("JSON input must contain a list of records.")

    if not all(isinstance(record, dict) for record in records):
        raise ValueError("Each JSON record must be an object.")

    return records


def validate_record(record):
    """Return a list of validation errors."""
    errors = []

    if not str(record.get("customer_id", "")).strip():
        errors.append("Missing customer ID")

    if not str(record.get("name", "")).strip():
        errors.append("Missing customer name")

    try:
        amount = float(record.get("amount", ""))

        if amount < 0:
            errors.append("Amount cannot be negative")

    except (ValueError, TypeError):
        errors.append("Amount must be a number")

    return errors


def process_records(records):
    """Separate valid records from invalid records."""
    valid_records = []
    exceptions = []

    for row_number, record in enumerate(records, start=2):
        errors = validate_record(record)

        if errors:
            exceptions.append({
                "row_number": row_number,
                "record": record,
                "errors": errors
            })
        else:
            record = record.copy()
            record["amount"] = float(record["amount"])
            valid_records.append(record)

    return valid_records, exceptions
