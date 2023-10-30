---
layout: page
title: netbsd/pkgin (English)
description: "Manage `pkgsrc` binary packages on NetBSD."
content_hash: 57e20dbd58db2ac0a929036c7c60a09ed13ff4ac
last_modified_at: 2023-10-30
---
# pkgin

Manage `pkgsrc` binary packages on NetBSD.
More information: <https://pkgin.net/#usage>.

- Install a package:

`pkgin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package and its dependencies:

`pkgin remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade all packages:

`pkgin full-upgrade`

- Search for a package:

`pkgin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- List installed packages:

`pkgin list`

- Remove unneeded dependencies:

`pkgin autoremove`
