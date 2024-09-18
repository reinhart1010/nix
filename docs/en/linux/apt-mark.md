---
layout: page
title: linux/apt-mark (English)
description: "Utility to change the status of installed packages."
content_hash: a69c2fdf7dd765678e373952769e305738490a74
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-mark.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-mark.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-mark.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-mark.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-mark.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-mark.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-mark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-mark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-mark

Utility to change the status of installed packages.
More information: <https://manned.org/apt-mark.8>.

- Mark a package as automatically installed:

`sudo apt-mark auto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Hold a package at its current version and prevent updates to it:

`sudo apt-mark hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Allow a package to be updated again:

`sudo apt-mark unhold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Show manually installed packages:

`apt-mark showmanual`

- Show held packages that aren't being updated:

`apt-mark showhold`
