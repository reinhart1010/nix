---
layout: page
title: linux/mkfs.ntfs (English)
description: "Creates a NTFS filesystem inside a partition."
content_hash: e581d6272dc14b45e01b1fc4b2e5d7f4e93c16c7
---
# mkfs.ntfs

Creates a NTFS filesystem inside a partition.
More information: <https://manned.org/mkfs.ntfs>.

- Create a NTFS filesystem inside partition 1 on device b (`sdb1`):

`mkfs.ntfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create filesystem with a volume-label:

`mkfs.ntfs -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create filesystem with specific UUID:

`mkfs.ntfs -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UUID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
