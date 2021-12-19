---
layout: page
title: linux/apt-get (English)
description: "Debian and Ubuntu package management utility."
content_hash: 74f3074531f19a0a4e7a744d88a93af5e594a3c7
related_topics:
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
---
# apt-get

Debian and Ubuntu package management utility.
Search for packages using `apt-cache`.
More information: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Update the list of available packages and versions (it's recommended to run this before other `apt-get` commands):

`apt-get update`

- Install a package, or update it to the latest available version:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package and its configuration files:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade all installed packages to their newest available versions:

`apt-get upgrade`

- Clean the local repository - removing package files (`.deb`) from interrupted downloads that can no longer be downloaded:

`apt-get autoclean`

- Remove all packages that are no longer needed:

`apt-get autoremove`

- Upgrade installed packages (like `upgrade`), but remove obsolete packages and install additional packages to meet new dependencies:

`apt-get dist-upgrade`
