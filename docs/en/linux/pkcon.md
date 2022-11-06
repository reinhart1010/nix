---
layout: page
title: linux/pkcon (English)
description: "Command line client for PackageKit console program used by Discover and Gnome software and alternative to 'apt'."
content_hash: 7e17195d11af3ee0f6379af717324a4354aee7a4
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pkcon

Command line client for PackageKit console program used by Discover and Gnome software and alternative to 'apt'.
More information: <https://manned.org/pkcon>.

- Install a package:

`pkcon install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package:

`pkcon remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Refresh the package cache:

`pkcon refresh`

- Update packages:

`pkcon update`

- Search for a specific package:

`pkcon search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List all available packages:

`pkcon get-packages`
