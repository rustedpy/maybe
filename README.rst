======
Maybe
======

.. image:: https://img.shields.io/github/actions/workflow/status/rustedpy/maybe/ci.yml?branch=master
    :alt: GitHub Workflow Status (branch)
    :target: https://github.com/rustedpy/maybe/actions/workflows/ci.yml?query=branch%3Amaster

.. image:: https://codecov.io/gh/rustedpy/maybe/branch/master/graph/badge.svg
    :alt: Coverage
    :target: https://codecov.io/gh/rustedpy/maybe

A simple Maybe (Option) type for Python 3 `inspired by Rust
<https://doc.rust-lang.org/std/option/>`__, fully type annotated.

Installation
============

Not yet available on PyPI. PyPI package coming soon.

Latest GitHub ``master`` branch version:

.. sourcecode:: sh

   $ pip install git+https://github.com/rustedpy/maybe

Summary
=======

**Experimental. API subject to change.**

The idea is that a possible value can be either ``Some(value)`` or
``Nothing()``, with a way to differentiate between the two. ``Some`` and
``Nothing`` are both classes encapsulating a possible value.

Example usage,

.. sourcecode:: Python

    from rustedpy-maybe import Nothing, Some

    o = Some('yay')
    n = Nothing()
    assert o.unwrap_or_else(str.upper) == 'yay'
    assert n.unwrap_or_else(lambda: 'default') == 'default'


License
=======

MIT License
