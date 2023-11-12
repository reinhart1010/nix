---
layout: page
title: linux/fdisk (English)
description: "A program for managing partition tables and partitions on a hard disk."
content_hash: 207bea12129277e2fb9d07a9537fe5f4e0401236
last_modified_at: 2023-11-12
related_topics:
  - title: हिन्दी version
    url: /hi/linux/fdisk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/fdisk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/fdisk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fdisk

A program for managing partition tables and partitions on a hard disk.
See also: `partprobe`.
More information: <https://manned.org/fdisk>.

- List partitions:

`sudo fdisk -l`

- Start the partition manipulator:

`sudo fdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Once partitioning a disk, create a partition:

`n`

- Once partitioning a disk, select a partition to delete:

`d`

- Once partitioning a disk, view the partition table:

`p`

- Once partitioning a disk, write the changes made:

`w`

- Once partitioning a disk, discard the changes made:

`q`

- Once partitioning a disk, open a help menu:

`m`
