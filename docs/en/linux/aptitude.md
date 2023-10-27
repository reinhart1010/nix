---
layout: page
title: linux/aptitude (English)
description: "Debian and Ubuntu package management utility."
content_hash: a63eb5dd2186fbacd8c4a244d66a0bff0fff71b8
last_modified_at: 2023-10-27
related_topics:
  - title: català version
    url: /ca/linux/aptitude.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/aptitude.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aptitude.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aptitude.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aptitude.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/aptitude.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/aptitude.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/aptitude.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
---
# aptitude

Debian and Ubuntu package management utility.
More information: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- Synchronize list of packages and versions available. This should be run first, before running subsequent `aptitude` commands:

`aptitude update`

- Install a new package and its dependencies:

`aptitude install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search for a package:

`aptitude search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search for an installed package (`?installed` is an `aptitude` search term):

`aptitude search '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`)'`

- Remove a package and all packages depending on it:

`aptitude remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade installed packages to the newest available versions:

`aptitude upgrade`

- Upgrade installed packages (like `aptitude upgrade`) including removing obsolete packages and installing additional packages to meet new package dependencies:

`aptitude full-upgrade`

- Put an installed package on hold to prevent it from being automatically upgraded:

`aptitude hold '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`)'`
