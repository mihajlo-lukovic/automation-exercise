# Test Automation Framework  
UI & API Test Suite for **Automation Exercise**  
https://automationexercise.com/

> **Python Version:** 3.13.3

---

## Table of Contents
- [About This Project](#about-this-project)
- [Virtual Environment](#virtual-environment)
- [Environment Variables (.env)](#environment-variables-env)
- [Installing Requirements](#installing-requirements)
- [How to Run Tests](#how-to-run-tests)
- [Technologies Used](#technologies-used)

---
## Recommended IDE
It is recommended to use **PyCharm** for working with this project, as it provides the most intuitive and powerful Python development experience, especially for running and debugging tests.

---

## About This Project

This repository contains a complete automated testing framework built to demonstrate practical UI and API test automation for the **Automation Exercise** website.

UI tests follow the **Page Object Model**, while API tests use clean request abstraction layers.  
All tests are executed using **Pytest**.

---

## Virtual Environment

Make sure to create a virtual environment before running the project.

---

## Environment Variables (.env)

Create a `.env` file in the project root to store path to chrome driver for testing; e.g. inside `.env` file -> `DRIVER=/Users/chromedriver`

---

## Installing Requirements

Activate the virtual environment and install all dependencies:
`pip install -r requirements.txt`

---

## How to Run Tests

#### Run all tests
> pytest

#### Run a specific dir
> pytest tests/ui

#### Run a specific file
> pytest tests/ui/test_cart.py

#### Generate HTML test report
> pytest --html=reports/test_report.html --self-contained-html

#### Use pyCharm editor:
You can run tests by clicking the `play` icon next to any test function or method inside a `.py` file, or by right-clicking on the test file, directory, function, or method and selecting `Run tests`.


---

## Technologies Used
* Python 3.13.3
* Pytest
* Selenium WebDriver
* Requests
* Faker
* pytest-html
* pytest-rerunfailures
