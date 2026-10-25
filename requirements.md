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

1. Read input records from supported data files.
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

The current sample input is `data/customers.csv`.

It contains these columns:

- `customer_id`
- `name`
- `amount`

The sample contains five customer records, including two intentionally invalid records.

## 6. Expected Outputs

- `output/valid_customers.csv` — valid customer records.
- `output/exception_report.csv` — invalid records and their validation errors.
- `output/process.log` — processing events and errors.

## 7. Quality and Acceptance Criteria

- The sample dataset contains five records.
- Three records pass validation.
- Two records fail validation.
- Invalid records include a clear reason for rejection.
- Missing input files are handled with an appropriate error.
- Automated tests pass successfully.
- The program can be run using the instructions in `README.md`.

## 8. Technology Stack

- Python
- Python CSV and pathlib modules
- Python logging module
- Pytest
- Visual Studio Code

## 9. Current Limitations and Future Improvements

- The current implementation processes CSV input. JSON input support remains to be implemented and tested.
- Additional tests can cover malformed files, missing columns, empty files, and unusual data values.
- Performance can be evaluated using larger datasets.
- The project can be extended with stronger configuration management and more comprehensive documentation.