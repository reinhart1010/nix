---
layout: page
title: linux/trizen (English)
description: "Arch Linux utility for building packages from the Arch User Repository (AUR)."
content_hash: 57ad4de75b19a6a20357a8d8c0b97d33913557e6
---
# trizen

Arch Linux utility for building packages from the Arch User Repository (AUR).
More information: <https://github.com/trizen/trizen>.

- Synchronize and update all AUR packages:

`trizen -Syua`

- Install a new package:

`trizen -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package and its dependencies:

`trizen -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search the package database for a keyword:

`trizen -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Show information about a package:

`trizen -Si `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List installed packages and versions:

`trizen -Qe`
