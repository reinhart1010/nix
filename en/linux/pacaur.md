---
layout: page
title: linux/pacaur (English)
description: "A utility for Arch Linux to build and install packages from the Arch User Repository."
content_hash: 557caa26e673e438c15edd271658c5b0085ec7f4
---
# pacaur

A utility for Arch Linux to build and install packages from the Arch User Repository.

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
