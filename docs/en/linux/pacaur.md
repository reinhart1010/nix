---
layout: page
title: linux/pacaur (English)
description: "A utility for Arch Linux to build and install packages from the Arch User Repository."
content_hash: f955a721036ac1b8a927e610d9796bdcb687af2c
---
# pacaur

A utility for Arch Linux to build and install packages from the Arch User Repository.
More information: <https://github.com/rmarquis/pacaur>.

- Synchronize and update all packages (includes AUR):

`pacaur -Syu`

- Synchronize and update only AUR packages:

`pacaur -Syua`

- Install a new package (includes AUR):

`pacaur -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a package and its dependencies (includes AUR packages):

`pacaur -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Search the package database for a keyword (includes AUR):

`pacaur -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- List all currently installed packages (includes AUR packages):

`pacaur -Qs`
