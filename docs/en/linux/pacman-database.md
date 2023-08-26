---
layout: page
title: linux/pacman-database (English)
description: "Operate on the Arch Linux package database."
content_hash: 8d7fb4ca97c2897541ea965d14d9eb54291ae5a3
last_modified_at: 2023-08-26
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-database.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-database.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-database.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-database.html
    icon: bi bi-globe
---
# pacman --database

Operate on the Arch Linux package database.
Modify certain attributes of the installed packages.
See also: `pacman`.
More information: <https://man.archlinux.org/man/pacman.8>.

- Mark a package as implicitly installed:

`sudo pacman --database --asdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Mark a package as explicitly installed:

`sudo pacman --database --asexplicit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Check that all the package dependencies are installed:

`pacman --database --check`

- Check the repositories to ensure all specified dependencies are available:

`pacman --database --check --check`

- Display only error messages:

`pacman --database --check --quiet`

- Display help:

`pacman --database --help`
