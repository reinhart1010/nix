---
layout: page
title: common/pylint (English)
description: "A Python code linter."
content_hash: c340977a92385c793e6a8775d6a2d328748b809d
---
# pylint

A Python code linter.
More information: <https://pylint.pycqa.org/en/latest/>.

- Show lint errors in a file:

`pylint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Lint a file and use a configuration file (usually named `pylintrc`):

`pylint --rcfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pylintrc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Lint a file and disable a specific error code:

`pylint --disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C,W,no-error,design</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
