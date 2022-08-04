---
layout: page
title: linux/partx (English)
description: "Parse a partition table and tell the kernel about it."
content_hash: 8d526d8f9b2651ae8812ac8681011632a3e33388
---
# partx

Parse a partition table and tell the kernel about it.
More information: <https://man7.org/linux/man-pages/man8/partx.8.html>.

- List the partitions on a block device or disk image:

`sudo partx --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_or_disk_image</span>

- Add all the partitions found in a given block device to the kernel:

`sudo partx --add --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_or_disk_image</span>

- Delete all the partitions found from the kernel (does not alter partitions on disk):

`sudo partx --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_or_disk_image</span>
