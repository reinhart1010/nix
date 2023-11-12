---
layout: page
title: linux/btrfs-check (English)
description: "Check or repair a btrfs filesystem."
content_hash: 33922f322217b40f584190343f3d32da510dff40
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/linux/btrfs-check.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-check.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs check

Check or repair a btrfs filesystem.
More information: <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

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
