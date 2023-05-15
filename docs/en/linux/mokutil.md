---
layout: page
title: linux/mokutil (English)
description: "Configure Secure Boot Machine Owner Keys (MOK)."
content_hash: 4976194c64aa71f0e71d84d888f18bdd2e18acec
last_modified_at: 2023-05-15
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mokutil

Configure Secure Boot Machine Owner Keys (MOK).
Some operations, such as enabling and disabling Secure Boot or enrolling keys require a reboot.
More information: <https://github.com/lcp/mokutil>.

- Show if Secure Boot is enabled:

`mokutil --sb-state`

- Enable Secure Boot:

`mokutil --enable-validation`

- Disable Secure Boot:

`mokutil --disable-validation`

- List enrolled keys:

`mokutil --list-enrolled`

- Enroll a new key:

`mokutil --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key.der</span>

- List the keys to be enrolled:

`mokutil --list-new`

- Set shim verbosity:

`mokutil --set-verbosity true`
