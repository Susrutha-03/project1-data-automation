import os
import csv
import logging
from pathlib import Path

from src.data_toolkit.processor import (
    read_csv,
    read_json,
    process_records,
)


BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = Path(
    os.getenv("INPUT_FILE", str(BASE_DIR / "data" / "customers.csv"))
)

OUTPUT_DIR = Path(
    os.getenv("OUTPUT_DIR", str(BASE_DIR / "output"))
)


def write_csv(file_path, records, fieldnames):
    """Write records to a CSV file."""
    with file_path.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=OUTPUT_DIR / "process.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
        force=True,
    )

    logger = logging.getLogger(__name__)

    try:
        logger.info("Data processing started.")

        if INPUT_FILE.suffix.lower() == ".json":
            records = read_json(INPUT_FILE)
        else:
            records = read_csv(INPUT_FILE)
        valid_records, exceptions = process_records(records)

        write_csv(
            OUTPUT_DIR / "valid_customers.csv",
            valid_records,
            ["customer_id", "name", "amount"],
        )

        exception_rows = []
        for item in exceptions:
            exception_rows.append({
                "row_number": item["row_number"],
                "customer_id": item["record"].get("customer_id", ""),
                "name": item["record"].get("name", ""),
                "amount": item["record"].get("amount", ""),
                "errors": "; ".join(item["errors"]),
            })

        write_csv(
            OUTPUT_DIR / "exception_report.csv",
            exception_rows,
            ["row_number", "customer_id", "name", "amount", "errors"],
        )

        logger.info("Total records: %s", len(records))
        logger.info("Valid records: %s", len(valid_records))
        logger.info("Invalid records: %s", len(exceptions))
        logger.info("Data processing completed successfully.")

        print(f"Total records: {len(records)}")
        print(f"Valid records: {len(valid_records)}")
        print(f"Invalid records: {len(exceptions)}")
        print("Reports and log saved in the output folder.")

    except Exception:
        logger.exception("Data processing failed.")
        raise


if __name__ == "__main__":
    main()
