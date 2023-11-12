---
layout: page
title: linux/checkupdates (English)
description: "Tool to check pending updates in Arch Linux."
content_hash: 3f2ce212a6bf72187591494f5c202617f8a5ac19
last_modified_at: 2023-11-12
related_topics:
  - title: हिन्दी version
    url: /hi/linux/checkupdates.html
    icon: bi bi-globe
tldri18n_status: 2
---
# checkupdates

Tool to check pending updates in Arch Linux.
More information: <https://man.archlinux.org/man/checkupdates.8>.

- List pending updates:

`checkupdates`

- List pending updates and download the packages to the pacman cache:

`checkupdates --download`

- List pending updates using a specific pacman database:

`CHECKUPDATES_DB=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` checkupdates`

- Display help:

`checkupdates --help`
