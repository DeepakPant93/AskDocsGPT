# Set the default target
.DEFAULT_GOAL := test

# Variables
PYTHON=python3
TEST_RUNNER=pytest

# Targets

# Default target to run all tests
.PHONY: all
all: test

# Target to run all tests
.PHONY: test
test:
	$(TEST_RUNNER)

# Target to run a specific test case
.PHONY: test-case
test-case:
	@if [ -z "$$TEST_CASE" ]; then \
		echo "Please set TEST_CASE variable to the test case name (e.g., make test-case TEST_CASE='service/test_qa_service.py::TestClassName::test_method_name')"; \
		exit 1; \
	fi
	$(TEST_RUNNER) $(TEST_CASE)

# Target to run tests from a specific module
.PHONY: test-module
test-module:
	@if [ -z "$$MODULE" ]; then \
		echo "Please set MODULE variable to the module name (e.g., make test-module MODULE='service')"; \
		exit 1; \
	fi
	$(TEST_RUNNER) $(MODULE)

# Target to clean __pycache__ directories
.PHONY: clean
clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
