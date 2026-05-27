# FakeStoreAPI Cart CRUD Automation Framework

API automation framework built using Python, Pytest, and Requests for testing Cart CRUD operations on FakeStoreAPI.

Target API:
https://fakestoreapi.com/

# Note : Known API Limitations / Observations

- GitHub Actions execution may intermittently fail due to public API rate limiting or cloud-runner restrictions resulting in HTTP 403 responses.
- FakeStoreAPI behaves as a public/mock API and some negative scenarios return successful responses instead of validation errors.
- Certain documented status codes differ from actual API responses.
- A few negative test cases are intentionally marked using `xfail` to document known API validation gaps.
- All tests execute successfully in the local environment.

# Framework Choice + Why

## Tech Stack

- Python
- Pytest
- Requests
- JSONSchema
- Pytest HTML Reports
- GitHub Actions
  
## Why Python?

Python was chosen because it provides a clean and readable syntax that helps accelerate automation framework development and maintenance. Its strong ecosystem support for Selenium, Pytest, and CI/CD integrations makes it highly suitable for scalable QA automation frameworks.
## Why Pytest?

Pytest was chosen because it provides:

- Simple and scalable test structure
- Powerful fixtures for reusable test data
- Built-in parametrization for data-driven testing
- Easy integration with reporting and CI/CD tools
- Clean assertion handling
- Faster test execution and maintainability

The Requests library was used for API interactions because it is lightweight, readable, and widely used for REST API automation.

# Extension Plan

## Parallelisation

The framework supports parallel test execution using `pytest-xdist`.

Benefits:
- Faster execution time
- Better scalability for large test suites
- Improved CI/CD efficiency

Example:

```bash
pytest -n 2
```

Future enhancement:
- Dynamic worker allocation based on CPU cores
- Distributed execution using Selenium Grid / containers

## Reporting

The framework currently supports HTML reporting using `pytest-html`.

Generated reports include:
- Execution summary
- Passed / Failed tests
- Assertion failure details
- Execution duration

Example:

```bash
pytest --html=reports/report.html --self-contained-html
```

Future enhancement:
- Allure reporting integration
- Email report notifications
- Historical trend reporting
- Dashboard integration for CI pipelines


# Test Coverage

The framework covers:

- Cart CRUD Operations
  - GET
  - POST
  - PUT
  - DELETE

- Positive Test Scenarios
- Negative Test Scenarios
- Authentication Testing
- Response Schema Validation
- Contract / Snapshot Testing
- Data-Driven Testing using multiple product IDs
- Response Time Validation


# Framework Features

- Reusable API Client
- Centralized Assertions
- Pytest Fixtures
- Schema Validation using JSONSchema
- Snapshot Contract Validation
- Parallel Execution Support
- HTML Reporting
- GitHub Actions CI Integration

# Project Structure

```text
fakestoreapi-cart-crud-tests/
│
├── .github/
│   └── workflows/
│       └── api-tests.yml
│
│       GitHub Actions workflow configuration
│       for automated CI test execution.
│
├── reports/
│   └── .gitkeep
│
│       Stores generated HTML execution reports.
│
├── schemas/
│   ├── cart_schema.json
│   ├── login_schema.json
│   └── product_schema.json
│
│       JSON schema files used for response
│       validation and contract verification.
│
├── snapshots/
│   └── product_snapshot.json
│
│       Snapshot contract files used to verify
│       API response structure consistency.
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_cart_delete.py
│   ├── test_cart_get.py
│   ├── test_cart_post.py
│   ├── test_cart_put.py
│   ├── test_data_driven.py
│   ├── test_schema_validation.py
│   └── test_snapshot_contract.py
│
│       Contains all API test cases including:
│       - CRUD validation
│       - Authentication testing
│       - Schema validation
│       - Snapshot testing
│       - Data-driven testing
│
├── utils/
│   ├── __init__.py
│   ├── api_client.py
│   ├── assertions.py
│   ├── config.py
│   └── helpers.py
│
│       Reusable utility modules containing:
│       - API request methods
│       - Custom assertions
│       - Configuration management
│       - Helper functions
│
├── .gitignore
│
│       Prevents unnecessary files and folders
│       from being committed to the repository.
│
├── pytest.ini
│
│       Pytest configuration file for:
│       - markers
│       - reporting
│       - test discovery
│
├── requirements.txt
│
│       Contains all Python dependencies
│       required to execute the framework.
│
└── README.md
```

Author

Nagaraju K
