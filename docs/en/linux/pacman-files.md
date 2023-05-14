---
layout: page
title: linux/pacman-files (English)
description: "Arch Linux package manager utility."
content_hash: b004a72e5d3afcc61d9cfcd6ed056f1efd826fa5
last_modified_at: 2023-05-14
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-files.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-files.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-files.html
    icon: bi bi-globe
---
# pacman --files

Arch Linux package manager utility.
See also `pkgfile`.
More information: <https://man.archlinux.org/man/pacman.8>.

- Update the package database:

`sudo pacman --files --refresh`

- Find the package that owns a specific file:

`pacman --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Find the package that owns a specific file, using a regular expression:

`pacman --files --regex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`'`

- List only the package names:

`pacman --files --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- List the files owned by a specific package:

`pacman --files --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Display help:

`pacman --files --help`
