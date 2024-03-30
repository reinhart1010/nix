---
layout: page
title: linux/mkfs.f2fs (English)
description: "Creates an F2FS filesystem inside a partition."
content_hash: 86c561cc362298de992510b2ed31343c879d4721
last_modified_at: 2024-03-30
tldri18n_status: 2
---
# mkfs.f2fs

Creates an F2FS filesystem inside a partition.
More information: <https://manned.org/mkfs.f2fs>.

- Create an F2FS filesystem inside partition 1 on device b (`sdb1`):

`sudo mkfs.f2fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create an F2FS filesystem with a volume label:

`sudo mkfs.f2fs -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
