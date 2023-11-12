---
layout: page
title: linux/pacman-sync (English)
description: "Arch Linux package manager utility."
content_hash: a7183cf5decaa231d6f53ab4baddf8998612f7fa
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-sync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-sync.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-sync.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-sync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --sync

Arch Linux package manager utility.
See also: `pacman`.
More information: <https://man.archlinux.org/man/pacman.8>.

- Install a new package:

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Synchronize and update all packages (add `--downloadonly` to download the packages and not update them):

`sudo pacman --sync --refresh --sysupgrade`

- Update all packages and install a new one without prompting:

`sudo pacman --sync --refresh --sysupgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search the package database for a regular expression or keyword:

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Display information about a package:

`pacman --sync --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Overwrite conflicting files during a package update:

`sudo pacman --sync --refresh --sysupgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Synchronize and update all packages, but ignore a specific package (can be used more than once):

`sudo pacman --sync --refresh --sysupgrade --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove not installed packages and unused repositories from the cache (use two `--clean` flags to clean all packages):

`sudo pacman --sync --clean`
