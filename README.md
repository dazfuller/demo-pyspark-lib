# Demo PySpark Library

This is a demo python library to support talks around Big Data Engineering and DevOps.

## Running tests and producing coverage

```powershell
# Inside the virtual environment

# Run tests and produce coverage information
python -m coverage run -m xmlrunner -o test-results discover -v -s ./tests -p test_*.py

# Generate coverage XML report
python -m coverage xml

# Generate coverage HTML report
python -m coverage html
```