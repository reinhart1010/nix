---
layout: page
title: linux/pacman-sync (English)
description: "Arch Linux package manager utility."
content_hash: 12edb943b5d85ac652bd89de36e5a18220215972
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-sync.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/pacman-sync.html
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
  - title: Nederlands version
    url: /nl/linux/pacman-sync.html
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

- [s]earch the package database for a regular expression or keyword:

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- Display [i]nformation about a package:

`pacman -Si `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Overwrite conflicting files during a package update:

`sudo pacman -Syu --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove not installed packages and unused repositories from the cache (use the flags `Sc` to [c]lean all packages):

`sudo pacman -Sc`

- Specify the package version that should be installed:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>
