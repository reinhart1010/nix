---
layout: page
title: linux/umount (English)
description: "Unlink a filesystem from its mount point, making it no longer accessible."
content_hash: 0bb097b97dcebe4ed13265ecf8e32247caff8bd6
last_modified_at: 2024-01-11
tldri18n_status: 2
---
# umount

Unlink a filesystem from its mount point, making it no longer accessible.
A filesystem cannot be unmounted when it is busy.
More information: <https://manned.org/umount.8>.

- Unmount a filesystem, by passing the path to the source it is mounted from:

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>

- Unmount a filesystem, by passing the path to the target where it is mounted:

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mounted_directory</span>

- When an unmount fails, try to remount the filesystem read-only:

`umount --read-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mounted_directory</span>

- Recursively unmount each specified directory:

`umount --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mounted_directory</span>

- Unmount all mounted filesystems (except the `proc` filesystem):

`umount -a`
