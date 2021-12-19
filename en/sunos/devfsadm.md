---
layout: page
title: sunos/devfsadm (English)
description: "Administration command for `/dev`. Maintains the `/dev` namespace."
content_hash: 3a726eaa27d63db7ec7643c4dbd58dd392760715
---
# devfsadm

Administration command for `/dev`. Maintains the `/dev` namespace.
More information: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Scan for new disks:

`devfsadm -c disk`

- Cleanup any dangling /dev links and scan for new device:

`devfsadm -C -v`

- Dry-run - output what would be changed but make no modifications:

`devfsadm -C -v -n`
