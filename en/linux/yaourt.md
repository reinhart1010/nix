---
layout: page
title: linux/yaourt (English)
description: "Arch Linux utility for building packages from the Arch User Repository."
content_hash: 2536c03094be46073f3d149153693cea755dedfc
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/yaourt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/yaourt.html
    icon: bi bi-globe
---
# yaourt

Arch Linux utility for building packages from the Arch User Repository.
More information: <https://linuxcommandlibrary.com/man/yaourt>.

- Synchronize and update all packages (including AUR):

`yaourt -Syua`

- Install a new package (includes AUR):

`yaourt -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a package and its dependencies (includes AUR packages):

`yaourt -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Search the package database for a keyword (including AUR):

`yaourt -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- List installed packages, versions, and repositories (AUR packages will be listed under the repository name 'local'):

`yaourt -Q`
