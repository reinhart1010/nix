---
layout: page
title: linux/btrfs-subvolume (English)
description: "Manage btrfs subvolumes and snapshots."
content_hash: f222b74fa89467dab3622fd624216b03f07deb16
related_topics:
  - title: 中文 version
    url: /zh/linux/btrfs-subvolume.html
    icon: bi bi-globe
---
# btrfs subvolume

Manage btrfs subvolumes and snapshots.
More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-subvolume>.

- Create a new empty subvolume:

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new_subvolume</span>

- List all subvolumes and snapshots in the specified filesystem:

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_filesystem</span>

- Delete a subvolume:

`sudo btrfs subvolume delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/subvolume</span>

- Create a read-only snapshot of an existing subvolume:

`sudo btrfs subvolume snapshot -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_subvolume</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target</span>

- Create a read-write snapshot of an existing subvolume:

`sudo btrfs subvolume snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_subvolume</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target</span>

- Show detailed information about a subvolume:

`sudo btrfs subvolume show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/subvolume</span>
