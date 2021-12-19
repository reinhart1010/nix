---
layout: page
title: linux/mkfs (English)
description: "Build a Linux filesystem on a hard disk partition."
content_hash: 807634959f735be39b828998902a5289e5a05bd2
related_topics:
  - title: italiano version
    url: /it/linux/mkfs.html
    icon: bi bi-globe
---
# mkfs

Build a Linux filesystem on a hard disk partition.
This command is deprecated in favor of filesystem specific mkfs.<type> utils.
More information: <https://manned.org/mkfs>.

- Build a Linux ext2 filesystem on a partition:

`mkfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Build a filesystem of a specified type:

`mkfs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ext4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Build a filesystem of a specified type and check for bad blocks:

`mkfs -c -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>
