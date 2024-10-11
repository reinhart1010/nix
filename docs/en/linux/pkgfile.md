---
layout: page
title: linux/pkgfile (English)
description: "Search files from packages in the official repositories on Arch-based systems."
content_hash: cb4d49e53686f75b222046d3bed725b8cd19cacb
last_modified_at: 2024-10-11
tldri18n_status: 2
---
# pkgfile

Search files from packages in the official repositories on Arch-based systems.
See also: `pacman files`, describing the usage of `pacman --files`.
More information: <https://manned.org/pkgfile>.

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
