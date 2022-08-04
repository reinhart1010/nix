---
layout: page
title: linux/btrfs-rescue (English)
description: "Try to recover a damaged btrfs filesystem."
content_hash: b73a2c06b4322d5178f8c7087b5b2c4204c83677
---
# btrfs rescue

Try to recover a damaged btrfs filesystem.
More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-rescue>.

- Rebuild the filesystem metadata tree (very slow):

`sudo btrfs rescue chunk-recover `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Fix device size alignment related problems (e.g. unable to mount the filesystem with super total bytes mismatch):

`sudo btrfs rescue fix-device-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Recover a corrupted superblock from correct copies (recover the root of filesystem tree):

`sudo btrfs rescue super-recover `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Recover from an interrupted transactions (fixes log replay problems):

`sudo btrfs rescue zero-log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/partition</span>

- Create a `/dev/btrfs-control` control device when `mknod` is not installed:

`sudo btrfs rescue create-control-device`
