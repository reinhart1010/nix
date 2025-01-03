---
layout: page
title: linux/pacman-database (English)
description: "Operate on the Arch Linux package database."
content_hash: 4d792533a9b660ee77da8f3eafe6b4e0262e76c8
last_modified_at: 2025-01-03
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-database.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/pacman-database.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-database.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-database.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-database.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman-database.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-database.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --database

Operate on the Arch Linux package database.
Modify certain attributes of the installed packages.
See also: `pacman`.
More information: <https://manned.org/pacman.8>.

- Mark a package as implicitly installed:

`sudo pacman -D --asdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Mark a package as explicitly installed:

`sudo pacman -D --asexplicit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Chec[k] that all the package dependencies are installed:

`pacman -Dk`

- Chec[k] the sync [D]atabase to ensure all specified dependencies of downloadable packages are available:

`pacman -Dkk`

- Chec[k] and display in [q]uiet mode (only error messages are displayed):

`pacman -Dkq`

- Display [h]elp:

`pacman -Dh`
