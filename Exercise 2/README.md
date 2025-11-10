```markdown
# CS 520 Exercise 2: Test Generation, Coverage, and Fault Detection

## Overview

This project is a demonstration of end-to-end unit testing strategy for algorithmic coding exercises. It covers:
- Measuring baseline coverage (line and branch)
- Using LLMs to improve test suites
- Fault detection via bug seeding

## Structure & Files

- Problem code files: `do_algebra.py`, `special_factorial.py`, etc.
- Unit test files: `test_do_algebra.py`, `test_special_factorial.py`, etc.
- Reports: Markdown, Word, or PDF as per assignment
- `README.md`: This file

## Environment Setup

1. **Create and activate your virtual environment:**
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
2. **Install dependencies:**
    ```
    pip install pytest pytest-cov
    ```

## Running Tests

All commands are run from the project directory.

### Run All Tests
```
python3 -m pytest
```

### Measure Line Coverage (all files)
```
python3 -m pytest --cov .
```

### Measure Branch Coverage (one module)
```
python3 -m pytest --cov=MODULE_NAME --cov-branch TEST_FILE.py
# Example:
python3 -m pytest --cov=do_algebra --cov-branch test_do_algebra.py
```

### Generate HTML Coverage Report
```
python3 -m pytest --cov=MODULE_NAME --cov-branch --cov-report html TEST_FILE.py
# Opens report in htmlcov/ directory (open htmlcov/index.html)
```




