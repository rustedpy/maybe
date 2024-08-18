# Maybe

[![GitHub Workflow Status (branch)](https://img.shields.io/github/actions/workflow/status/rustedpy/maybe/ci.yml?branch=master)](https://github.com/rustedpy/maybe/actions/workflows/ci.yml?query=branch%3Amaster)
[![Coverage](https://codecov.io/gh/rustedpy/maybe/branch/master/graph/badge.svg)](https://codecov.io/gh/rustedpy/maybe)

A simple Maybe (Option) type for Python 3 [inspired by Rust](
https://doc.rust-lang.org/std/option/), fully type annotated.

## Installation

Latest release:

```sh
pip install rustedpy-maybe
```

Latest GitHub `master` branch version:

```sh
pip install git+https://github.com/rustedpy/maybe
```

## Summary

**Experimental. API subject to change.**

The idea is that a possible value can be either `Some(value)` or `Nothing()`,
with a way to differentiate between the two. `Some` and `Nothing` are both
classes encapsulating a possible value.

Example usage,

```python
from maybe import Nothing, Some

o = Some('yay')
n = Nothing()
assert o.unwrap_or_else(str.upper) == 'yay'
assert n.unwrap_or_else(lambda: 'default') == 'default'
```

There are some methods that support conversion from a `Maybe` to a `Result` type
in the `result` package.  If you wish to leverage these methods, you must add
`result` to your dependency list:

```python
from maybe import Nothing, Some
from result import Ok, Err

o = Some('yay')
n = Nothing()
assert o.ok_or('error') == Ok('yay')
assert o.ok_or_else(lambda: 'error') == Ok('yay')
assert n.ok_or('error') == Err('error')
assert n.ok_or_else(lambda: 'error') == Err('error')
```

## Contributing

These steps should work on any Unix-based system (Linux, macOS, etc) with Python
and `make` installed. On Windows, you will need to refer to the Python
documentation (linked below) and reference the `Makefile` for commands to run
from the non-unix shell you're using on Windows.

1. Setup and activate a virtual environment.  See [Python docs][pydocs-venv] for
   more information about virtual environments and setup.
1. Run `make install` to install dependencies
1. Switch to a new git branch and make your changes
1. Test your changes:
   - `make test`
   - `make lint`
   - You can also start a Python REPL and import `maybe`
1. Update documentation
   - Edit any relevant docstrings, markdown files
   - Run `make docs`
1. Add an entry to the [changelog](./CHANGELOG.md)
1. Git commit all your changes and create a new PR.

[pydocs-venv]: https://docs.python.org/3/library/venv.html

## License

MIT License
