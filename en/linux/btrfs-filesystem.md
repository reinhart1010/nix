---
layout: page
title: linux/btrfs-filesystem (English)
description: "Manage btrfs filesystems."
content_hash: af1da897c0286b32964f3e565ba8e718321b7dc9
related_topics:
  - title: 中文 version
    url: /zh/linux/btrfs-filesystem.html
    icon: bi bi-globe
---
# btrfs filesystem

Manage btrfs filesystems.
More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-filesystem>.

- Show filesystem usage (optionally run as root to show detailed information):

`btrfs filesystem usage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_mount</span>

- Show usage by individual devices:

`sudo btrfs filesystem show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_mount</span>

- Defragment a single file on a btrfs filesystem (avoid while a deduplication agent is running):

`sudo btrfs filesystem defragment -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Defragment a directory recursively (does not cross subvolume boundaries):

`sudo btrfs filesystem defragment -v -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Force syncing unwritten data blocks to disk(s):

`sudo btrfs filesystem sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_mount</span>

- Summarize disk usage for the files in a directory recursively:

`sudo btrfs filesystem du --summarize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
