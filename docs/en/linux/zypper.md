---
layout: page
title: linux/zypper (English)
description: "SUSE & openSUSE package management utility."
content_hash: 924f49b6b4b8279c61e1ef8b9fa3c574802179f1
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/zypper.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/zypper.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/zypper.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/zypper.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/zypper.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/zypper.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/zypper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zypper

SUSE & openSUSE package management utility.
For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
More information: <https://en.opensuse.org/SDB:Zypper_manual>.

- Synchronize list of packages and versions available:

`zypper refresh`

- Install a new package:

`zypper install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package:

`zypper remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade installed packages to the newest available versions:

`zypper update`

- Search package via keyword:

`zypper search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Show information related to configured repositories:

`zypper repos --sort-by-priority`
