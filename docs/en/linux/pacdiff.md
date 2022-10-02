---
layout: page
title: linux/pacdiff (English)
description: "Maintenance utility for `.pacorig`, `.pacnew` and `.pacsave` files created by `pacman`."
content_hash: 05e27a4957b9fa76e6537938ebf5b4328faa6c2e
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pacdiff

Maintenance utility for `.pacorig`, `.pacnew` and `.pacsave` files created by `pacman`.
More information: <https://man.archlinux.org/man/pacdiff>.

- Review files that need maintenance in interactive mode:

`pacdiff`

- Use sudo and sudoedit to remove and merge files:

`pacdiff --sudo`

- Review files needing maintenance, creating `.bak`ups of the original if you `(O)verwrite`:

`pacdiff --sudo --backup`

- Use a specific editor to view and merge configuration files (default is `vim -d`):

`DIFFPROG=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">editor</span>` pacdiff`

- Scan for configuration files with `locate` instead of using pacman database:

`pacdiff --locate`

- Display help:

`pacdiff --help`
