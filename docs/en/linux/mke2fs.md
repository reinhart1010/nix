---
layout: page
title: linux/mke2fs (English)
description: "Create a Linux filesystem inside a partition."
content_hash: 5a082afc329d151c675d81fcd8f862c9fd876072
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# mke2fs

Create a Linux filesystem inside a partition.
More information: <https://manned.org/mke2fs>.

- Create an ext2 filesystem in partition 1 of device b (`sdb1`):

`mkfs.ext2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create an ext3 filesystem in partition 1 of device b (`sdb1`):

`mkfs.ext3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create an ext4 filesystem in partition 1 of device b (`sdb1`):

`mkfs.ext4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
