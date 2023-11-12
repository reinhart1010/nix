---
layout: page
title: linux/pacman-deptest (English)
description: "Check each dependency specified and return a list of dependencies that are not currently satisfied on the system."
content_hash: ee4e0b7e913e402a50d155af7fcfaec12fba80a3
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-deptest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --deptest

Check each dependency specified and return a list of dependencies that are not currently satisfied on the system.
See also: `pacman`.
More information: <https://man.archlinux.org/man/pacman.8>.

- Print the package names of the dependencies that aren't installed:

`pacman --deptest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Check if the installed package satisfies the given minimum version:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>=5</span>`"`

- Check if a later version of a package is installed:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>5</span>`"`

- Display help:

`pacman --deptest --help`
