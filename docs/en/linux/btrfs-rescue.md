---
layout: page
title: linux/btrfs-rescue (English)
description: "Try to recover a damaged btrfs filesystem."
content_hash: b66024cbc51864b310271348cfbbb7a931db1bdf
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/linux/btrfs-rescue.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-rescue.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs rescue

Try to recover a damaged btrfs filesystem.
More information: <https://btrfs.readthedocs.io/en/latest/btrfs-rescue.html>.

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
