
import pytest

from src.data_toolkit.processor import (
    read_csv,
    read_json,
    validate_record,
    process_records,
)


def test_valid_record():
    record = {"customer_id": "101", "name": "Ravi", "amount": "250"}
    assert validate_record(record) == []


def test_missing_name():
    record = {"customer_id": "102", "name": "", "amount": "100"}
    assert "Missing customer name" in validate_record(record)


def test_negative_amount():
    record = {"customer_id": "103", "name": "Anu", "amount": "-50"}
    assert "Amount cannot be negative" in validate_record(record)


def test_process_records():
    records = [
        {"customer_id": "101", "name": "Ravi", "amount": "250"},
        {"customer_id": "102", "name": "", "amount": "100"},
    ]
    valid, exceptions = process_records(records)
    assert len(valid) == 1
    assert len(exceptions) == 1


def test_read_csv_missing_file(tmp_path):
    missing_file = tmp_path / "missing.csv"
    with pytest.raises(FileNotFoundError):
        read_csv(missing_file)


def test_read_json(tmp_path):
    json_file = tmp_path / "customers.json"
    json_file.write_text(
        '[{"customer_id": "101", "name": "Ravi", "amount": 250}]',
        encoding="utf-8",
    )

    records = read_json(json_file)

    assert len(records) == 1
    assert records[0]["name"] == "Ravi"


def test_read_json_missing_file(tmp_path):
    missing_file = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError):
        read_json(missing_file)


def test_read_json_invalid_format(tmp_path):
    json_file = tmp_path / "invalid.json"
    json_file.write_text(
        "{invalid json}",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        read_json(json_file)


def test_read_json_rejects_non_list(tmp_path):
    json_file = tmp_path / "object.json"
    json_file.write_text(
        '{"customer_id": "101", "name": "Ravi", "amount": 250}',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="must contain a list"):
        read_json(json_file)


def test_read_json_rejects_non_object_record(tmp_path):
    json_file = tmp_path / "invalid_record.json"
    json_file.write_text(
        '["not a record"]',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Each JSON record must be an object"):
        read_json(json_file)


