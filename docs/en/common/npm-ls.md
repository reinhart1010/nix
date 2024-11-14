---
layout: page
title: common/npm-ls (English)
description: "Print installed packages to `stdout`."
content_hash: 47bdabb461207153702f90dc6982c792508b98ef
last_modified_at: 2024-11-14
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-ls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm ls

Print installed packages to `stdout`.
More information: <https://docs.npmjs.com/cli/commands/npm-ls>.

- Print all versions of direct dependencies to `stdout`:

`npm ls`

- Print all installed packages including peer dependencies:

`npm ls --all`

- Print dependencies with extended information:

`npm ls --long`

- Print dependencies in parseable format:

`npm ls --parseable`

- Print dependencies in JSON format:

`npm ls --json`
