# AskDocsGPT - Server Module Unit Tests

This directory contains unit test cases for the **server module** of the **AskDocsGPT** project. We have used both `pytest` and `unittest` libraries to write and organize the test cases effectively. The tests cover the core functionality of the AskDocsGPT backend services.

## Prerequisites

To run the test cases, make sure you have the following installed:
- Python 3.10+
- `pytest` for running test cases
- `pytest-cov` for test coverage
- `allure-pytest` for generating reports
- `unittest` for isolated and asynchronous test cases

## Setup

Before running the tests, ensure all the necessary dependencies are installed. You can install them by running the following command:

```bash
pip install -r requirements.txt
```

## Test Configuration

The `pytest.ini` file is included in the project for configuring pytest and its related plugins. This file contains settings like test discovery patterns and coverage options.

### Sample pytest.ini Configuration

```ini
[pytest]
minversion = 6.0
addopts = -ra -q
testpaths = tests
pythonpath = src
asyncio_default_fixture_loop_scope = function
filterwarnings =
    ignore::DeprecationWarning
    ignore::UserWarning:langchain.*
```

## Running the Tests

We have included a [Makefile](Makefile) to make running tests and generating reports simpler. Here are the key commands you can use:

### Makefile Commands

You can run all the test cases using the following `make` command:


| Command                                 | Description                                                                                                              |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `make`                                  | Runs all the unit tests using `pytest`.                                                                                  |
| `make test`                             | Runs all the unit tests using `pytest`.                                                                                  |
| `make test-case TEST_CASE=<test-file>`  | Runs all the unit tests from the specific file using `pytest` e.g `make test-case TEST_CASE=service/test_qa_service.py`. |
| `make test-module MODULE=<module_name>` | Runs all the unit tests from the specific module using `pytest` e.g. `make test-module MODULE=service`.                  |
| `make coverage`                         | Runs the tests and displays test coverage.                                                                               |
| `make report`                           | Runs the tests and generates an Allure HTML report.                                                                      |


This will run the tests, collect the report data, and generate an Allure HTML report, which can be viewed for detailed insights into the test results.

## Additional Notes
To run the Allure report, you need to install Allure. Here are the commands to install Allure on Linux, Windows, and Mac:

| **Operating System** | **Command to Install Allure**                                                                                                                   |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Linux**            | Install via package manager: <br> ```sudo apt-add-repository ppa:qameta/allure``` <br> ```sudo apt update``` <br> ```sudo apt install allure``` |
| **Windows**          | Install via Scoop (recommended): <br> ```scoop install allure```                                                                                |
| **Mac**              | Install using Homebrew: <br> ```brew install allure```                                                                                          |

Use `allure --version` to confirm that Allure has been installed correctly on your system.

