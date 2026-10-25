# Business Data Automation Toolkit

## 1. Project Overview

The Business Data Automation Toolkit is a Python application that reads customer data from CSV and JSON files, validates records, separates valid and invalid data, and generates output reports.

## 2. Features

- Reads customer records from CSV files.
- Reads customer records from JSON files.
- Validates customer IDs and names.
- Checks that amounts are numeric and non-negative.
- Separates valid and invalid records.
- Generates a CSV file containing valid records.
- Generates an exception report with row numbers and error messages.
- Logs processing activity and errors.
- Supports configurable input and output paths using environment variables.
- Includes automated tests using pytest.

## 3. Project Structure

```text
project1_data_automation/
├── data/
│   ├── customers.csv
│   └── customers.json
├── output/
│   ├── valid_customers.csv
│   ├── exception_report.csv
│   └── process.log
├── src/
│   └── data_toolkit/
│       ├── __init__.py
│       └── processor.py
├── tests/
│   └── test_processor.py
├── main.py
├── README.md
└── requirements.md
```

## 4. Requirements

- Python 3
- pytest for automated testing

Install pytest if necessary:

```bash
python -m pip install pytest
```

## 5. How to Run

Open a terminal in the project root directory.

Run the application with CSV input:

```powershell
$env:INPUT_FILE = "data/customers.csv"
python main.py
```

Run the application with JSON input:

```powershell
$env:INPUT_FILE = "data/customers.json"
python main.py
```

## 6. Output Files

- `output/valid_customers.csv` — records that pass validation.
- `output/exception_report.csv` — invalid records and their validation errors.
- `output/process.log` — processing activity and errors.

The output files are overwritten each time the application runs.

## 7. Run Automated Tests

From the project root:

```powershell
python -m pytest tests -q
```

The tests cover record validation, record processing, CSV file errors, JSON reading, and invalid JSON input.

## 8. Validation Rules

1. Customer ID must not be empty.
2. Customer name must not be empty.
3. Amount