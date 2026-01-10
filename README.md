# unit-integration-testing-lab

**Student Name:** Javairia Waseem
**Roll Number:** 231400097

## Project Description

This project implements unit and integration tests for a simple banking application.  
It includes functionalities like deposit, withdraw, interest calculation, loan eligibility, and fund transfer between accounts.  

## How to Run Tests

1. Make sure Python and `pytest` are installed.
To run unit tests, execute: pytest test_unit.py
To run integration tests, execute: pytest test_integration.py
2. Install dependencies:
    ```bash
    pip install -r requirements.txt

## GitHub Actions Description

This repository uses GitHub Actions to automate testing.  
On every push or pull request, the workflow automatically runs the unit and integration tests to ensure code quality.  
The workflow sets up a Python environment, installs dependencies from `requirements.txt`, and runs tests using `pytest`.  
