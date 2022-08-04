---
layout: page
title: linux/btrfs-check (English)
description: "Check or repair a btrfs filesystem."
content_hash: c30d55bff174bcd75b4a9309c2012490b8321f52
---
# btrfs check

Check or repair a btrfs filesystem.
More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-check>.

- Check a btrfs filesystem:

`sudo btrfs check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Check and repair a btrfs filesystem (dangerous):

`sudo btrfs check --repair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Show the progress of the check:

`sudo btrfs check --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Verify the checksum of each data block (if the filesystem is good):

`sudo btrfs check --check-data-csum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Use the `n`-th superblock (`n` can be 0, 1 or 2):

`sudo btrfs check --super `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Rebuild the checksum tree:

`sudo btrfs check --repair --init-csum-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Rebuild the extent tree:

`sudo btrfs check --repair --init-extent-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>
