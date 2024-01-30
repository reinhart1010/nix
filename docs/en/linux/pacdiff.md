---
layout: page
title: linux/pacdiff (English)
description: "Maintenance utility for `.pacorig`, `.pacnew` and `.pacsave` files created by `pacman`."
content_hash: c8dff6b80f9d9d66a92f9fb2ebaa5f7868c8a6f9
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# pacdiff

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

- Scan for configuration files with `locate` instead of using `pacman` database:

`pacdiff --locate`

- Display help:

`pacdiff --help`
