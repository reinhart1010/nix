---
layout: page
title: linux/navi (English)
description: "An interactive cheatsheet tool for the command line and application launchers."
content_hash: 06e5d7a71bcb2271fe617a790cdf0f50e038fb08
last_modified_at: 2024-02-25
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/navi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># navi

An interactive cheatsheet tool for the command line and application launchers.
More information: <https://github.com/denisidoro/navi>.

- Browse through all available cheatsheets:

`navi`

- Browse the cheatsheet for `navi` itself:

`navi fn welcome`

- Print a command from the cheatsheet without executing it:

`navi --print`

- Output shell widget source code (It automatically detects your shell if possible, but can also be specified manually):

`navi widget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell</span>

- Autoselect and execute the snippet that best matches a query:

`navi --query '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`' --best-match`
