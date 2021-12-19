---
layout: page
title: linux/vgscan (English)
description: "Scan for volume groups on all supported Logical Volume Manager (LVM) block devices."
content_hash: 5c5e528e57e150c918d6da5fb59d20d96d1a353e
---
# vgscan

Scan for volume groups on all supported Logical Volume Manager (LVM) block devices.
See also `lvm`, `vgchange`.
More information: <https://manned.org/vgscan>.

- Scan for volume groups and print information about each group found:

`sudo vgscan`

- Scan for volume groups and add the special files in `/dev`, if they don't already exist, needed to access the logical volumes in the found groups :

`sudo vgscan --mknodes`
