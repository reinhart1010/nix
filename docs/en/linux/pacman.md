---
layout: page
title: linux/pacman (English)
description: "Arch Linux package manager utility."
content_hash: edce3a4095407b9a8a7ce0daae36f537b3d0577f
last_modified_at: 2024-12-28
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/pacman.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/pacman.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman

Arch Linux package manager utility.
See also: `pacman-sync`, `pacman-remove`, `pacman-query`, `pacman-upgrade`, `pacman-files`, `pacman-database`, `pacman-deptest`, `pacman-key`, `pacman-mirrors`.
For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
More information: <https://manned.org/pacman.8>.

- [S]ynchronize and update all packages:

`sudo pacman -Syu`

- Install a new package:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- [R]emove a package and its dependencies:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search ([s]) the package database for a regular expression or keyword:

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Search the database for packages containing a specific [F]ile:

`pacman -F "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_name</span>`"`

- List only the [e]xplicitly installed packages and versions:

`pacman -Qe`

- List orphan packages (installed as [d]ependencies but not actually required by any package):

`pacman -Qtdq`

- Empty the entire `pacman` cache:

`sudo pacman -Scc`
