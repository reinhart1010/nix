---
layout: page
title: common/fusermount (English)
description: "Mount and unmount FUSE filesystems."
content_hash: 25c221ea01390073a68642af7219e5e9e1158f8c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# fusermount

Mount and unmount FUSE filesystems.
More information: <https://manned.org/fusermount>.

- Unmount a FUSE filesystem:

`fusermount -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Unmount a FUSE filesystem as soon as it becomes unused:

`fusermount -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Display version:

`fusermount --version`
