# Demo PySpark Library

[![Build Status](https://dev.azure.com/dazfuller/Talks/_apis/build/status/demo-pyspark-lib?branchName=main)](https://dev.azure.com/dazfuller/Talks/_build/latest?definitionId=10&branchName=main)

This is a demo python library to support talks around Big Data Engineering and DevOps.

The repository contains a simple library for Spark 3 which provides some simple functions such as parsing Excel dates, and standardising column names.

This is also meant to show the source code being stored in Github, but with the pipelines, environments, and secrets being configured in [Azure DevOps](https://dev.azure.com).

## Setting up locally

The code has been built against Python 3.7 (as this matches Databricks runtime 7) and so it is advised that this is the version used. There are no features in use however which would prevent the usage of Python 3.6 and above.

You will need to create a virtual environment. The coverage configuration expects this to be at `.venv` but it can be anything, just remember to update `.coveragerc` to reflect your virtual environment location.

### Windows

```powershell
# Create the python virtual environment and activate it
python -m venv .venv

# Alternatively, if you have multiple versions of python installed
py -3.7 -m venv .venv

# Activate the virtual environment
.\.venv\scripts\active # Or activate.ps1 if using Powershell
```

### Linux/Mac

On a Linux environment you may need to install the python venv package separately. On Debian based distributions this might look something like.

```bash
sudo apt install python3-venv
```

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Finally

_N.B._ To deactivate your virtual environment just type `deactivate` and press enter.

Once your virtual environment is set up then make sure you update pip and install the package dependencies. These will include the development dependencies as well.

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

This project uses [Flake8](https://flake8.pycqa.org/) with the `pep8-naming` package for code linting. It uses [Coverage.py](https://coverage.readthedocs.io/) for producing code coverage reports, and it uses [xmlrunner](https://github.com/xmlrunner/unittest-xml-reporting) for running the unit tests and producing JUnit style reports for Azure Pipelines to consume.

All unit tests are writting the [unittest](https://docs.python.org/3/library/unittest.html) framework which is part of the standard library. This is just because I happen to like it.

Also in use is the [Rope](https://github.com/python-rope/rope) refactoring library which is used by [Visual Studio Code](https://code.visualstudio.com) for performaing refactoring activities such as variable renaming.

### Visual Studio Code

The library was developed using Visual Studio Code, and so an `extensions.json` file exists to provide quick access to the extensions the author feels are needed for building on this library. To access these simply open the Extensions panel, and type in `@recommended` in the search bar, this will show the workspace recommendations. These are _not_ mandatory, but can make development a bit easier.

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
