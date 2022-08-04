---
layout: page
title: linux/auracle (English)
description: "Command-line tool used to interact with Arch Linux's User Repository, commonly referred to as the AUR."
content_hash: 8e3b0399cb85593d0a8414d976ef67fd57d989fa
related_topics:
  - title: 中文 version
    url: /zh/linux/auracle.html
    icon: bi bi-globe
---
# auracle

Command-line tool used to interact with Arch Linux's User Repository, commonly referred to as the AUR.
More information: <https://github.com/falconindy/auracle>.

- Display AUR packages that match a regular expression:

`auracle search '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`'`

- Display package information for a space-separated list of AUR packages:

`auracle info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package2</span>

- Display the `PKGBUILD` file (build information) for a space-separated list of AUR packages:

`auracle show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package2</span>

- Display updates for installed AUR packages:

`auracle outdated`
