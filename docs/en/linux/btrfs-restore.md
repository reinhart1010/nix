---
layout: page
title: linux/btrfs-restore (English)
description: "Try to salvage files from a damaged btrfs filesystem."
content_hash: 8afaa02960fe6daa7f7aea792125825d959bb7dd
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/linux/btrfs-restore.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-restore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs restore

Try to salvage files from a damaged btrfs filesystem.
More information: <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- Restore all files from a btrfs filesystem to a given directory:

`sudo btrfs restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- List (don't write) files to be restored from a btrfs filesystem:

`sudo btrfs restore --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- Restore files matching a given regex ([c]ase-insensitive) files to be restored from a btrfs filesystem (all parent directories of target file(s) must match as well):

`sudo btrfs restore --path-regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- Restore files from a btrfs filesystem using a specific root tree `bytenr` (see `btrfs-find-root`):

`sudo btrfs restore -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bytenr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- Restore files from a btrfs filesystem (along with metadata, extended attributes, and Symlinks), overwriting files in the target:

`sudo btrfs restore --metadata --xattr --symlinks --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>
