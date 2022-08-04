---
layout: page
title: common/tlmgr-conf (English)
description: "Manage the TeX Live configuration."
content_hash: 675927da180a6454454a9ecfc03c3cb4972cd653
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tlmgr conf

Manage the TeX Live configuration.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- Show the current TeX Live configuration:

`tlmgr conf`

- Show the current `texmf`, `tlmgr`, or `updmap` configuration:

`tlmgr conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texmf|tlmgr|updmap</span>

- Show only a specific configuration option:

`tlmgr conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texmf|tlmgr|updmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_key</span>

- Set a specific configuration option:

`tlmgr conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texmf|tlmgr|updmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Delete a specific configuration option:

`tlmgr conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texmf|tlmgr|updmap</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_key</span>

- Disable the execution of system calls via `\write18`:

`tlmgr conf texmf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_escape</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>

- Show all additional `texmf` trees:

`tlmgr conf auxtrees show`
