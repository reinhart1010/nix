---
layout: page
title: common/pytest (English)
description: "Run Python tests."
content_hash: adf9208c301fadff5d5139574c7a8c23cf50e17f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pytest

Run Python tests.
More information: <https://docs.pytest.org/>.

- Run tests from specific files:

`pytest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test_file1.py path/to/test_file2.py ...</span>

- Run tests with names matching a specific [k]eyword expression:

`pytest -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression</span>

- Exit as soon as a test fails or encounters an error:

`pytest --exitfirst`

- Run tests matching or excluding markers:

`pytest -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">marker_name1 and not marker_name2</span>

- Run until a test failure, continuing from the last failing test:

`pytest --stepwise`

- Run tests without capturing output:

`pytest --capture=no`
