---
layout: page
title: linux/swapon (English)
description: "Enables device or file for swapping."
content_hash: 6c936945495927ad8ae741514dd7ebce9275ca9e
---
# swapon

Enables device or file for swapping.
More information: <https://manned.org/swapon>.

- Get swap information:

`swapon -s`

- Enable a given swap partition:

`swapon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb7</span>

- Enable a given swap file:

`swapon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Enable all swap areas:

`swapon -a`

- Enable swap by label of a device or file:

`swapon -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">swap1</span>
