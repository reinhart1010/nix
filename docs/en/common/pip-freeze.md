---
layout: page
title: common/pip-freeze (English)
description: "List installed packages in requirements format."
content_hash: 6abdf5e4ecd7a360d1d35e7ef32c6830f4df3a73
last_modified_at: 2024-02-04
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pip-freeze.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pip freeze

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
