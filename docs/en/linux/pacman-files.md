---
layout: page
title: linux/pacman-files (English)
description: "Arch Linux package manager utility."
content_hash: 8c0042d9908202268218223b980993ea3697d219
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-files.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-files.html
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

- List only the absolute path to the files:

`pacman --query --list --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Display help:

`pacman --files --help`
