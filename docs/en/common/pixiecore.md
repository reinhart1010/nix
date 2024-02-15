---
layout: page
title: common/pixiecore (English)
description: "Manage the network booting of machines."
content_hash: 129cec0239c313827bbcf011703435b9b9f24b6a
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# pixiecore

Manage the network booting of machines.
More information: <https://github.com/danderson/netboot/tree/master/pixiecore>.

- Start a PXE boot server which provides a `netboot.xyz` boot image:

`pixiecore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quick</span>` xyz --dhcp-no-bind`

- Start a new PXE boot server which provides an Ubuntu boot image:

`pixiecore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quick</span>` ubuntu --dhcp-no-bind`

- List all available boot images for quick mode:

`pixiecore quick --help`
