 # PyRTT
A pylink based package for interacting with JLink's RTT utility.

## Pipelines

[![build](
https://github.com//haydenridd/pyrtt/workflows/ci/badge.svg)](
https://github.com//haydenridd/pyrtt/actions?query=workflow%3Aci)

## Installation

### Base package
To install the package for use run:
```commandline
pip install pyrtt
```

### Development
To install required dependencies for development run:
```commandline
pip install -r requirements.txt
```

You are now ready to use and/or develop the package.

## Building and Testing

Pytest suite can be run by calling `pytest` in the root directory.
Package can be built into a tarball using `python setup.py sdist` in the root directory.

## Usage

Example below:

```python

def main():
    pass

if __name__ == '__main__':
    main()

```

## Contributing

This project was developed using Python version 3.11.1. You can either use the built in package manager (pip), or Anaconda
to install required modules from requirements.txt file. See 
[this link](https://pip.pypa.io/en/stable/user_guide/#requirements-files) on how to install packages from a 
requirements.txt file using pip. See 
[this link](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) on how to create 
an environment in Anaconda from a requirements.txt file.

This project is using the [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) 
workflow. To contribute please create a `feature/your-feature` branch off of `main` branch and submit a Pull Request.

## Authors
Hayden Riddiford
