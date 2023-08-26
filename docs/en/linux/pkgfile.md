---
layout: page
title: linux/pkgfile (English)
description: "Tool for searching files from packages in the official repositories on arch-based systems."
content_hash: 971eab98f87f15dbd7ae45d4ce6ad2a9a099f994
last_modified_at: 2023-08-26
---
# pkgfile

Tool for searching files from packages in the official repositories on arch-based systems.
See also `pacman files`, describing the usage of `pacman --files`.
More information: <https://man.archlinux.org/man/extra/pkgfile/pkgfile.1>.

- Synchronize the pkgfile database:

`sudo pkgfile --update`

- Search for a package that owns a specific file:

`pkgfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- List all files provided by a package:

`pkgfile --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List executables provided by a package:

`pkgfile --list --binaries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search for a package that owns a specific file using case-insensitive matching:

`pkgfile --ignorecase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Search for a package that owns a specific file in the `bin` or `sbin` directory:

`pkgfile --binaries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Search for a package that owns a specific file, displaying the package version:

`pkgfile --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Search for a package that owns a specific file in a specific repository:

`pkgfile --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>
