---
layout: page
title: linux/pacman-deptest (English)
description: "Check each dependency specified and return a list of dependencies that are not currently satisfied on the system."
content_hash: dcdd9a0a29b0fc752f290edb06c7aedeb7799257
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-deptest.html
    icon: bi bi-globe
---
# pacman --deptest

Check each dependency specified and return a list of dependencies that are not currently satisfied on the system.
More information: <https://man.archlinux.org/man/pacman.8>.

- Print the package names of the dependencies that aren't installed:

`pacman --deptest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name2</span>

- Check if the installed package satisfies the given minimum version:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>=5</span>`"`

- Check if a later version of a package is installed:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>5</span>`"`

- Display help:

`pacman --deptest --help`
