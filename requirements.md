# Business Data Automation Toolkit — Requirements

## 1. Project Overview

The Business Data Automation Toolkit is a Python application designed to read business data, validate records, transform data, and generate reports for valid and invalid records.

## 2. Problem Statement

Manual checking of business data can be time-consuming and can allow incorrect records to go unnoticed. This toolkit aims to automate validation and reporting to improve data quality and reduce repetitive work.

## 3. Target Users

- Business data entry teams
- Data analysts
- Small businesses processing customer records

## 4. Functional Requirements

1. Read input records from CSV and JSON files.
2. Validate customer IDs and customer names.
3. Check that amounts are numeric and non-negative.
4. Separate valid records from invalid records.
5. Generate a CSV file containing valid records.
6. Generate an exception report containing invalid records and explanations.
7. Record processing activity and errors in a log file.
8. Allow input and output paths to be configured using environment variables.
9. Handle missing input files and other processing errors.
10. Support automated tests for important processing functions.

## 5. Input Data

The project includes two sample input files:

- `data/customers.csv`
- `data/customers.json`

The CSV sample contains five customer records, including two intentionally invalid records.

The JSON sample contains four customer records, including two intentionally invalid records.

The customer records use these fields:

- `customer_id`
- `name`
- `amount`

## 6. Expected Outputs

- `output/valid_customers.csv` — valid customer records.
- `output/exception_report.csv` — invalid records and their validation errors.
- `output/process.log` — processing events and errors.

## 7. Quality and Acceptance Criteria

- The CSV sample contains five records.
- Three CSV records pass validation.
- Two CSV records fail validation.
- The JSON sample can also be processed.
- Invalid records include a clear reason for rejection.
- Missing input files are handled with an appropriate error.
- Automated tests pass successfully.
- The program can be run using the instructions in `README.md`.

## 8. Technology Stack

- Python
- Python `csv`, `json`, and `pathlib` modules
- Python `logging` module
- pytest
- Visual Studio Code

## 9. Current Limitations and Future Improvements

- The current implementation supports CSV and JSON input.
- Additional tests can cover missing CSV columns, empty files, and unusual data values.
- Performance can be evaluated using larger datasets.
- The project can be extended with stronger configuration management and more comprehensive documentation.
