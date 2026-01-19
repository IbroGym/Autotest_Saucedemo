# QA Assignment 5 — SauceDemo UI Automation (PyTest + Selenium)

## Project Overview
This project contains automated UI tests for the SauceDemo website using:
- Python
- Selenium WebDriver
- PyTest
- Python logging
- pytest-html (HTML execution report)
- Automatic screenshots on test failure

Test System: https://www.saucedemo.com/

---

## Prerequisites
- Python 3.x installed
- Google Chrome installed
- Internet connection

---

## Setup Instructions (Windows PowerShell)

## 1) Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

## 2) Install dependencies
python -m pip install --upgrade pip
python -m pip install selenium pytest webdriver-manager pytest-html

## Running Tests
-- Run all tests --
python -m pytest -v

-- Run a single test file --
python -m pytest -v test_login.py

-- Generate HTML Test Execution Report -- 
python -m pytest -v --html=report.html --self-contained-html

After execution, the report will be created: report.html

## Logs and Screenshots
# Logs

Logs are written automatically to the logs/ folder.
Each run creates a new log file: logs/test_run_<timestamp>.log

# Screenshots

Screenshots are captured automatically on test failure.
Files are stored in the screenshots/ folder.
Screenshot path is also recorded in the log.
