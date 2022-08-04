---
layout: page
title: linux/xbps (English)
description: "The X Binary Package System (or xbps) is the binary package system used by Void Linux."
content_hash: 089218409ae4f134a5c24bf6e1b7a68967c62ded
---
# xbps

The X Binary Package System (or xbps) is the binary package system used by Void Linux.
More information: <https://github.com/void-linux/xbps>.

- Install packages and synchronize them with the remote repository:

`xbps-install --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name2</span>

- Search for a package in the remote repository:

`xbps-query --repository -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a package, leaving all of its dependencies installed:

`xbps-remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a package and all of its dependencies recursively that are not required by other packages:

`xbps-remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Synchronize your repository databases and update your system and dependencies:

`xbps-install --sync --update`

- Remove packages that were installed as dependencies and aren't currently needed:

`xbps-remove --remove-orphans`

- Remove obsolete packages from the cache:

`xbps-remove --clean-cache`
