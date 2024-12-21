---
layout: page
title: linux/pacman-query (English)
description: "Arch Linux package manager utility."
content_hash: c66bde20c45ed72d6a2ac4c646080622a6aa9973
last_modified_at: 2024-12-21
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-query.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-query.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-query.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman-query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --query

Arch Linux package manager utility.
See also: `pacman`.
More information: <https://manned.org/pacman.8>.

- [Q]uery the local package database and list installed packages and versions:

`pacman -Q`

- List only packages and versions that were [e]xplicitly installed:

`pacman -Qe`

- Find which package [o]wns a file:

`pacman -Qo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Display information about an [i]nstalled package:

`pacman -Qi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display the [l]ist of files owned by a specific package:

`pacman -Ql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List orphan packages (installed as [d]ependencies but unrequired ([t]) by any package and print in [q]uiet mode (only package name is displayed)):

`pacman -Qdtq`

- List installed packages foreign ([m]) to the repository database:

`pacman -Qm`

- List packages that can be [u]pgraded:

`pacman -Qu`
