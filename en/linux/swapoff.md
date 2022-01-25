---
layout: page
title: linux/swapoff (English)
description: "Disables device or file for swapping."
content_hash: 9030f1c4f6fbebd0b6f1b3d86c7a21f8bf0570da
---
# swapoff

Disables device or file for swapping.
More information: <https://manned.org/swapoff>.

- Disable a given swap partition:

`swapoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb7</span>

- Disable a given swap file:

`swapoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Disable all swap areas:

`swapoff -a`

- Disable swap by label of a device or file:

`swapoff -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">swap1</span>
