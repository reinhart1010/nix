---
layout: page
title: common/pip-freeze (English)
description: "List installed packages in requirements format."
content_hash: 6abdf5e4ecd7a360d1d35e7ef32c6830f4df3a73
last_modified_at: 2024-02-05
tldri18n_status: 2
---
# pip freeze

List installed packages in requirements format.
More information: <https://pip.pypa.io/en/stable/cli/pip_freeze>.

- List installed packages:

`pip freeze`

- List installed packages and write it to the `requirements.txt` file:

`pip freeze > requirements.txt`

- List installed packages in a virtual environment, excluding globally installed packages:

`pip freeze --local > requirements.txt`

- List installed packages in the user-site:

`pip freeze --user > requirements.txt`

- List all packages, including `pip`, `distribute`, `setuptools`, and `wheel` (they are skipped by default):

`pip freeze --all > requirements.txt`
