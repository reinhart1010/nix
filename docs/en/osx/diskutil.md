---
layout: page
title: osx/diskutil (English)
description: "Utility to manage local disks and volumes."
content_hash: 1ceef2f597e63aef8bb57b80cb7b53a948800b1f
related_topics:
  - title: italiano version
    url: /it/osx/diskutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/diskutil.html
    icon: bi bi-globe
---
# diskutil

Utility to manage local disks and volumes.
More information: <https://ss64.com/osx/diskutil.html>.

- List all currently available disks, partitions and mounted volumes:

`diskutil list`

- Repair the filesystem data structures of a volume:

`diskutil repairVolume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Unmount a volume:

`diskutil unmountDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Eject a CD/DVD (unmount first):

`diskutil eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk1</span>
