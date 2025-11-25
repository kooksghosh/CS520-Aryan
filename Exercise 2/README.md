# Exercise 2 Testing Procedure Locally



## Environment Setup

1. **Create and activate a virtual environment**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
2. **Install required dependencies**

   ```bash
   pip install pytest pytest-cov
   ```

---

## Running Tests

All commands should be run from the project’s root directory.

### Run all tests

```bash
python3 -m pytest
```

### Measure Line Coverage (all files)

```bash
python3 -m pytest --cov .
```


### Measure Branch Coverage (one module)

```bash
python3 -m pytest --cov=MODULE_NAME --cov-branch TEST_FILE.py
Example:
python3 -m pytest --cov=do_algebra --cov-branch test_do_algebra.py
```

### Generate HTML Coverage Report
```bash
python3 -m pytest --cov=MODULE_NAME --cov-branch --cov-report html TEST_FILE.py
```
Then open the generated `htmlcov/index.html` in a browser.

