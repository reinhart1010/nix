---
layout: page
title: linux/pacaur (English)
description: "A utility for Arch Linux to build and install packages from the Arch User Repository."
content_hash: b50948ad847b29dfc0e5b266aeedb02daf6499a9
last_modified_at: 2023-08-26
---
# pacaur

A utility for Arch Linux to build and install packages from the Arch User Repository.
More information: <https://github.com/rmarquis/pacaur>.

- Synchronize and update all packages (includes AUR):

`pacaur -Syu`

- Synchronize and update only AUR packages:

`pacaur -Syua`

- Install a new package (includes AUR):

`pacaur -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package and its dependencies (includes AUR packages):

`pacaur -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search the package database for a keyword (includes AUR):

`pacaur -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- List all currently installed packages (includes AUR packages):

`pacaur -Qs`
