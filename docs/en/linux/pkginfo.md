---
layout: page
title: linux/pkginfo (English)
description: "Query the package database on a CRUX system."
content_hash: 14ecfd31cca3ab5dbaed5b8f801a8b34b7b675c0
last_modified_at: 2023-08-26
---
# pkginfo

Query the package database on a CRUX system.
More information: <https://crux.nu/Main/Handbook3-6#ntoc19>.

- List installed packages and their versions:

`pkginfo -i`

- List files owned by a package:

`pkginfo -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List the owner(s) of files matching a pattern:

`pkginfo -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Print the footprint of a file:

`pkginfo -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
