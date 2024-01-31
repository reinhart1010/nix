---
layout: page
title: linux/auracle (English)
description: "Command-line tool used to interact with Arch Linux's User Repository, commonly referred to as the AUR."
content_hash: 3d2ed65e4396d9abe5515329218114489023efcb
last_modified_at: 2024-01-31
related_topics:
  - title: 中文 version
    url: /zh/linux/auracle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# auracle

Command-line tool used to interact with Arch Linux's User Repository, commonly referred to as the AUR.
More information: <https://github.com/falconindy/auracle>.

- Display AUR packages that match a regular expression:

`auracle search '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`'`

- Display information about one or more AUR packages:

`auracle info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Display the `PKGBUILD` file (build information) of one or more AUR packages:

`auracle show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Display updates for installed AUR packages:

`auracle outdated`
