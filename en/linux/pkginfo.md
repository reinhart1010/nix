---
layout: page
title: linux/pkginfo (English)
description: "Query the package database on a CRUX system."
content_hash: fa78f94ba1416e1b718a56eb3309dabc225358a6
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

`pkginfo -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
