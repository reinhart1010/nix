---
layout: page
title: linux/pacman-files (English)
description: "Arch Linux package manager utility."
content_hash: 30f9eb64e2a43d505ed7ef1d60046ebc23e3c79b
last_modified_at: 2024-11-30
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-files.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-files.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-files.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-files.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman-files.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-files.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --files

Arch Linux package manager utility.
See also: `pacman`, `pkgfile`.
More information: <https://manned.org/pacman.8>.

- Update the package database:

`sudo pacman -Fy`

- Find the package that owns a specific [F]ile:

`pacman -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Find the package that owns a specific [F]ile, using a regular e[x]pression:

`pacman -Fx '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`'`

- List only the package names:

`pacman -Fq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- [l]ist the [F]iles owned by a specific package:

`pacman -Fl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display [h]elp:

`pacman -Fh`
