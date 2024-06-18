---
layout: page
title: linux/partx (English)
description: "Parse a partition table and tell the kernel about it."
content_hash: 43ad6a763c8b056060bdd0c4039097dfb7ca4e9e
last_modified_at: 2024-06-18
tldri18n_status: 2
---
# partx

Parse a partition table and tell the kernel about it.
More information: <https://manned.org/partx>.

- List the partitions on a block device or disk image:

`sudo partx --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_or_disk_image</span>

- Add all the partitions found in a given block device to the kernel:

`sudo partx --add --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_or_disk_image</span>

- Delete all the partitions found from the kernel (does not alter partitions on disk):

`sudo partx --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_or_disk_image</span>
