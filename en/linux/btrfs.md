---
layout: page
title: linux/btrfs (English)
description: "A filesystem based on the copy-on-write (COW) principle for Linux."
content_hash: 02823c6e8bb87d54e0c05fdade97f872b0b08c67
related_topics:
  - title: 中文 version
    url: /zh/linux/btrfs.html
    icon: bi bi-globe
---
# btrfs

A filesystem based on the copy-on-write (COW) principle for Linux.
Some subcommands such as `btrfs device` have their own usage documentation.
More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs>.

- Create subvolume:

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/subvolume</span>

- List subvolumes:

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Show space usage information:

`sudo btrfs filesystem df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Enable quota:

`sudo btrfs quota enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/subvolume</span>

- Show quota:

`sudo btrfs qgroup show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/subvolume</span>
