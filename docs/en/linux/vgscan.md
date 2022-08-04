---
layout: page
title: linux/vgscan (English)
description: "Scan for volume groups on all supported Logical Volume Manager (LVM) block devices."
content_hash: 8a9cc8dad7bd145f60c133062e2419423b01362b
---
# vgscan

Scan for volume groups on all supported Logical Volume Manager (LVM) block devices.
See also `lvm`, `vgchange`.
More information: <https://manned.org/vgscan>.

- Scan for volume groups and print information about each group found:

`sudo vgscan`

- Scan for volume groups and add the special files in `/dev`, if they don't already exist, needed to access the logical volumes in the found groups:

`sudo vgscan --mknodes`
