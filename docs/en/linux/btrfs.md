---
layout: page
title: linux/btrfs (English)
description: "A filesystem based on the copy-on-write (COW) principle for Linux."
content_hash: d06f4352baf40f7e05c166fb19eaed71e243c008
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/linux/btrfs.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/btrfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs

A filesystem based on the copy-on-write (COW) principle for Linux.
Some subcommands such as `btrfs device` have their own usage documentation.
More information: <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

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
