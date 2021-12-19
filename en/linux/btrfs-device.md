---
layout: page
title: linux/btrfs-device (English)
description: "Manage devices in a btrfs filesystem."
content_hash: c8a28e920a9cae38299b3af0e7bbfb8dd4334f8a
related_topics:
  - title: 中文 version
    url: /zh/linux/btrfs-device.html
    icon: bi bi-globe
---
# btrfs device

Manage devices in a btrfs filesystem.
More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-device>.

- Add one or more devices to a btrfs filesystem:

`sudo btrfs device add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/block_device1</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/block_device2</span>`] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_filesystem</span>

- Remove a device from a btrfs filesystem:

`sudo btrfs device remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device|device_id</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>`]`

- Display error statistics:

`sudo btrfs device stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_filesystem</span>

- Scan all disks and inform the kernel of all detected btrfs filesystems:

`sudo btrfs device scan --all-devices`

- Display detailed per-disk allocation statistics:

`sudo btrfs device usage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_filesystem</span>
