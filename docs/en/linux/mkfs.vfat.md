---
layout: page
title: linux/mkfs.vfat (English)
description: "Creates an MS-DOS filesystem inside a partition."
content_hash: 9ca3c706aed1ecfb774968adde0eb730e2fbaacf
---
# mkfs.vfat

Creates an MS-DOS filesystem inside a partition.
More information: <https://manned.org/mkfs.vfat>.

- Create a vfat filesystem inside partition 1 on device b (`sdb1`):

`mkfs.vfat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create filesystem with a volume-name:

`mkfs.vfat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create filesystem with a volume-id:

`mkfs.vfat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Use 5 instead of 2 file allocation tables:

`mkfs.vfat -f 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
