---
layout: page
title: common/ruff-format (English)
description: "An extremely fast Python code formatter."
content_hash: f1c248085708e6045707da4302ff1d1b51f80cc9
last_modified_at: 2024-02-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ruff-format.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ruff format

An extremely fast Python code formatter.
If no files or directories are specified, the current working directory is used by default.
More information: <https://docs.astral.sh/ruff/formatter>.

- Format given files or directories in-place:

`ruff format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Print which files would have been modified and return a non-zero exit code if there are files to reformat, and zero otherwise:

`ruff format --check`

- Print what changes would be made without modifying the files:

`ruff format --diff`
