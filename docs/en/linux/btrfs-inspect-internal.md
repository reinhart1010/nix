---
layout: page
title: linux/btrfs-inspect-internal (English)
description: "Query internal information of a btrfs filesystem."
content_hash: c860b08bc287841d6b458eda97eeb347d356661c
---
# btrfs inspect-internal

Query internal information of a btrfs filesystem.
More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-inspect-internal>.

- Print superblock's information:

`sudo btrfs inspect-internal dump-super `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Print superblock's and all of its copies' information:

`sudo btrfs inspect-internal dump-super --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Print filesystem's metadata information:

`sudo btrfs inspect-internal dump-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Print list of files in inode `n`-th:

`sudo btrfs inspect-internal inode-resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_mount</span>

- Print list of files at a given logical address:

`sudo btrfs inspect-internal logical-resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_mount</span>

- Print stats of root, extent, csum and fs trees:

`sudo btrfs inspect-internal tree-stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>
