---
layout: page
title: common/pylint (English)
description: "A Python code linter."
content_hash: 55d825985829643d47c0f063113e3a4056b46a4f
last_modified_at: 2024-05-29
tldri18n_status: 2
---
# pylint

A Python code linter.
More information: <https://pylint.pycqa.org/en/latest/>.

- Show lint errors in a file:

`pylint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Lint a package or module (must be importable; no `.py` suffix):

`pylint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_or_module</span>

- Lint a package from a directory path (must contain an `__init__.py` file):

`pylint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Lint a file and use a configuration file (usually named `pylintrc`):

`pylint --rcfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pylintrc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Lint a file and disable a specific error code:

`pylint --disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C,W,no-error,design</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
