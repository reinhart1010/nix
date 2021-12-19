---
layout: page
title: common/fusermount (English)
description: "Mount and unmount FUSE filesystems."
content_hash: 705d99d1b7b431883adfe21c210c28eb6ed3cbbf
---
# fusermount

Mount and unmount FUSE filesystems.
More information: <https://man.archlinux.org/man/fusermount.1>.

- Unmount a FUSE filesystem:

`fusermount -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Unmount a FUSE filesystem as soon as it becomes unused:

`fusermount -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Display version:

`fusermount --version`
