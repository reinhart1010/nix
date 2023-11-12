---
layout: page
title: linux/mke2fs (English)
description: "Creates a Linux filesystem inside a partition."
content_hash: 8e36624e3374c0fbb1f01c8876ed1b4626edf49a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mke2fs

Creates a Linux filesystem inside a partition.
More information: <https://manned.org/mke2fs>.

- Create an ext2 filesystem in partition 1 of device b (`sdb1`):

`mkfs.ext2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create an ext3 filesystem in partition 1 of device b (`sdb1`):

`mkfs.ext3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create an ext4 filesystem in partition 1 of device b (`sdb1`):

`mkfs.ext4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
