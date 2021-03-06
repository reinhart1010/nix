---
layout: page
title: linux/pacman-mirrors (English)
description: "Generate a pacman mirrorlist for Manjaro Linux."
content_hash: ed87966b7f8aaf63997bc0b9a824e5ce27b910d7
related_topics:
  - title: français version
    url: /fr/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-mirrors.html
    icon: bi bi-globe
---
# pacman-mirrors

Generate a pacman mirrorlist for Manjaro Linux.
Every run of pacman-mirrors requires you to synchronize your database and update your system using `sudo pacman -Syyu`.
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
