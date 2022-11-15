---
layout: page
title: linux/mkfs.btrfs (English)
description: "Create a btrfs filesystem."
content_hash: 79a241e798f88ca67c896fa09f3dde736246739b
related_topics:
  - title: Indonesia version
    url: /id/linux/mkfs.btrfs.html
    icon: bi bi-globe
---
# mkfs.btrfs

Create a btrfs filesystem.
Defaults to `raid1`, which specifies 2 copies of a given data block spread across 2 different devices.
More information: <https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html>.

- Create a btrfs filesystem on a single device:

`sudo mkfs.btrfs --metadata single --data single `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- Create a btrfs filesystem on multiple devices with raid1:

`sudo mkfs.btrfs --metadata raid1 --data raid1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdN</span>

- Set a label for the filesystem:

`sudo mkfs.btrfs --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdN</span>`]`
