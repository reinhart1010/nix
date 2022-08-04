---
layout: page
title: common/umount (English)
description: "Unlink a filesystem from its mount point, making it no longer accessible."
content_hash: 33a547d07947156b19b590b17e9f1676e6be14f1
---
# umount

Unlink a filesystem from its mount point, making it no longer accessible.
A filesystem cannot be unmounted when it is busy.
More information: <https://manned.org/umount.8>.

- Unmount a filesystem, by passing the path to the source it is mounted from:

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>

- Unmount a filesystem, by passing the path to the target where it is mounted:

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mounted_directory</span>

- Unmount all mounted filesystems (except the `proc` filesystem):

`umount -a`
