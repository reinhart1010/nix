---
layout: page
title: osx/diskutil (English)
description: "Utility to manage local disks and volumes."
content_hash: a284012e49138b320258ea7d2a80ee9c756f828a
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/osx/diskutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/diskutil.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/diskutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/diskutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/diskutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diskutil

Utility to manage local disks and volumes.
More information: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- List all currently available disks, partitions and mounted volumes:

`diskutil list`

- Repair the filesystem data structures of a volume:

`diskutil repairVolume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk_device</span>

- Unmount a volume:

`diskutil unmountDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk_device</span>

- Eject a CD/DVD (unmount first):

`diskutil eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk_device1</span>
