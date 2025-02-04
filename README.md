[![tests](https://github.com/Ciela-Institute/caustic/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/Ciela-Institute/caustic/actions)
[![Docs](https://github.com/Ciela-Institute/caustic/actions/workflows/documentation.yaml/badge.svg)](https://github.com/Ciela-Institute/caustic/actions/workflows/documentation.yaml)
[![PyPI version](https://badge.fury.io/py/caustic.svg)](https://pypi.org/project/caustic/)
[![coverage](https://img.shields.io/codecov/c/github/Ciela-Institute/caustic)](https://app.codecov.io/gh/Ciela-Institute/caustic)
# caustic

The lensing pipeline of the future: GPU-accelerated, automatically-differentiable,
highly modular. Currently under heavy development: expect interface changes and
some imprecise/untested calculations.

## Installation 

Simply install caustic from PyPI:
```bash
pip install caustic
```

## Documentation

Please see our [documentation page](Ciela-Institute.github.io/caustic/) for more detailed information.

## Contributing

Please reach out to one of us if you're interested in contributing!

To start, follow the installation instructions, replacing the last line with
```bash
pip install -e ".[dev]"
```
This creates an editable install and installs the dev dependencies.

Some guidelines:
- Please use `isort` and `black` to format your code.
- Use `CamelCase` for class names and `snake_case` for variable and method names.
- Open up issues for bugs/missing features.
- Use pull requests for additions to the code.
- Write tests that can be run by [`pytest`](https://docs.pytest.org/).
