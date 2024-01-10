---
layout: page
title: common/umount (English)
description: "Unlink a filesystem from its mount point, making it no longer accessible."
content_hash: aac28e8d8323ab9e4320d05001a3d430adefa05c
last_modified_at: 2024-01-10
related_topics:
  - title: 한국어 version
    url: /ko/common/umount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# umount

Unlink a filesystem from its mount point, making it no longer accessible.
A filesystem cannot be unmounted when it is busy.
More information: <https://man.openbsd.org/umount>.

- Unmount a filesystem, by passing the path to the source it is mounted from:

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>

- Unmount a filesystem, by passing the path to the target where it is mounted:

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mounted_directory</span>

- Unmount all mounted filesystems (except the `proc` filesystem):

`umount -a`
