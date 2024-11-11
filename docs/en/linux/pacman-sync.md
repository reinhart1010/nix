---
layout: page
title: linux/pacman-sync (English)
description: "Arch Linux package manager utility."
content_hash: a08a5fb7d45cec684f76f643a0f8d31dfb550aef
last_modified_at: 2024-11-11
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
  - title: 한국어 version
    url: /ko/linux/pacman-sync.html
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
More information: <https://manned.org/pacman.8>.

- Install a new package:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- [S]ynchronize and refresh ([y]) the package database along with a sys[u]pgrade (add `--downloadonly` to only download the packages and not update them):

`sudo pacman -Syu`

- Update and [u]pgrade all packages and install a new one without prompting:

`sudo pacman -Syu --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search ([s]) the package database for a regular expression or keyword:

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Display [i]nformation about a package:

`pacman -Si `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Overwrite conflicting files during a package update:

`sudo pacman -Syu --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- [S]ynchronize and [u]pdate all packages, but ignore a specific package (can be used more than once):

`sudo pacman -Syu --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove not installed packages and unused repositories from the cache (use the flags `Scc` to [c]lean all packages):

`sudo pacman -Sc`
