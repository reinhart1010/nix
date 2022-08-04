---
layout: page
title: linux/pacman-database (English)
description: "Operate on the Arch Linux package database."
content_hash: 86a0cfd2d1c237843bbe0e541d7f8c5f5e2fb879
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-database.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-database.html
    icon: bi bi-globe
---
# pacman --database

Operate on the Arch Linux package database.
Modify certain attributes of the installed packages.
More information: <https://man.archlinux.org/man/pacman.8>.

- Display help:

`pacman --database --help`

- Mark a package as implicitly installed:

`sudo pacman --database --asdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Mark a package as explicitly installed:

`sudo pacman --database --asexplicit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Check that all the package dependencies are installed:

`pacman --database --check`

- Check the repositories to ensure all specified dependencies are available:

`pacman --database --check --check`

- Display only error messages:

`pacman --database --check --quiet`
