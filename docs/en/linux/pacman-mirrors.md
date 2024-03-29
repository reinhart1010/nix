---
layout: page
title: linux/pacman-mirrors (English)
description: "Generate a `pacman` mirrorlist for Manjaro Linux."
content_hash: 36e6213a6af06f40122c1630840439cb62c46370
last_modified_at: 2024-01-30
related_topics:
  - title: français version
    url: /fr/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-mirrors.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman-mirrors

Generate a `pacman` mirrorlist for Manjaro Linux.
Every run of `pacman-mirrors` requires you to synchronize your database and update your system using `sudo pacman -Syyu`.
See also: `pacman`.
More information: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Generate a mirrorlist using the default settings:

`sudo pacman-mirrors --fasttrack`

- Get the status of the current mirrors:

`pacman-mirrors --status`

- Display the current branch:

`pacman-mirrors --get-branch`

- Switch to a different branch:

`sudo pacman-mirrors --api --set-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|unstable|testing</span>

- Generate a mirrorlist, only using mirrors in your country:

`sudo pacman-mirrors --geoip`
