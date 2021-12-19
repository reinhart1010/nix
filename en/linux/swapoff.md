---
layout: page
title: linux/swapoff (English)
description: "Disables device or file for swapping."
content_hash: c7c5c5df57c90655481f7652a8572eb699169b9c
---
# swapoff

Disables device or file for swapping.

- Disable a given swap partition:

`swapoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb7</span>

- Disable a given swap file:

`swapoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Disable all swap areas:

`swapoff -a`

- Disable swap by label of a device or file:

`swapoff -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">swap1</span>
