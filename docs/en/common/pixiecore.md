---
layout: page
title: common/pixiecore (English)
description: "Tool to manage the network booting of machines."
content_hash: a1b370c87e91c6f30626aeaccf5dc022c921fd3a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pixiecore

Tool to manage the network booting of machines.
More information: <https://github.com/danderson/netboot/tree/master/pixiecore>.

- Start a PXE boot server which provides a `netboot.xyz` boot image:

`pixiecore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quick</span>` xyz --dhcp-no-bind`

- Start a new PXE boot server which provides an Ubuntu boot image:

`pixiecore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quick</span>` ubuntu --dhcp-no-bind`

- Get a list of all available boot images for quick mode:

`pixiecore quick --help`
