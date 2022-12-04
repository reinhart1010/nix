---
layout: page
title: linux/pkginfo (English)
description: "Query the package database on a CRUX system."
content_hash: 56997caed5b2ca86a33294fcf3a7e382d4203c69
last_modified_at: 2022-12-04
---
# pkginfo

Query the package database on a CRUX system.
More information: <https://crux.nu/Main/Handbook3-6#ntoc19>.

- List installed packages and their versions:

`pkginfo -i`

- List files owned by a package:

`pkginfo -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- List the owner(s) of files matching a pattern:

`pkginfo -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Print the footprint of a file:

`pkginfo -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
