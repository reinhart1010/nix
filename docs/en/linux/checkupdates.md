---
layout: page
title: linux/checkupdates (English)
description: "Check pending updates in Arch Linux."
content_hash: 143912fe941720a924248af2fe1931456dfa6cd6
last_modified_at: 2024-02-15
related_topics:
  - title: हिन्दी version
    url: /hi/linux/checkupdates.html
    icon: bi bi-globe
tldri18n_status: 2
---
# checkupdates

Check pending updates in Arch Linux.
More information: <https://man.archlinux.org/man/checkupdates.8>.

- List pending updates:

`checkupdates`

- List pending updates and download the packages to the `pacman` cache:

`checkupdates --download`

- List pending updates using a specific `pacman` database:

`CHECKUPDATES_DB=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` checkupdates`

- Display help:

`checkupdates --help`
