---
layout: page
title: linux/vgscan (English)
description: "Scan for volume groups on all supported Logical Volume Manager (LVM) block devices."
content_hash: 91792ffef196eb51b43a61e16f2eedf68bb268ac
last_modified_at: 2023-11-23
tldri18n_status: 2
---
# vgscan

Scan for volume groups on all supported Logical Volume Manager (LVM) block devices.
See also: `lvm` and `vgchange`.
More information: <https://manned.org/vgscan>.

- Scan for volume groups and print information about each group found:

`sudo vgscan`

- Scan for volume groups and add the special files in `/dev`, if they don't already exist, needed to access the logical volumes in the found groups:

`sudo vgscan --mknodes`
