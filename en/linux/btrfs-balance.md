---
layout: page
title: linux/btrfs-balance (English)
description: "Balance block groups on a btrfs filesystem."
content_hash: a3e0f84520ac43ff8c35593c0fae530fd0a1c690
---
# btrfs balance

Balance block groups on a btrfs filesystem.
More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-balance>.

- Show the status of a running or paused balance operation:

`sudo btrfs balance status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_filesystem</span>

- Balance all block groups (slow; rewrites all blocks in filesystem):

`sudo btrfs balance start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_filesystem</span>

- Balance data block groups which are less than 15% utilized, running the operation in the background:

`sudo btrfs balance start --bg -dusage=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_filesystem</span>

- Balance a max of 10 metadata chunks with less than 20% utilization and at least 1 chunk on a given device `devid` (see `btrfs filesystem show`):

`sudo btrfs balance start -musage=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>`,limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`,devid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">devid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_filesystem</span>

- Convert data blocks to the raid6 and metadata to raid1c3 (see mkfs.btrfs(8) for profiles):

`sudo btrfs balance start -dconvert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raid6</span>` -mconvert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raid1c3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_filesystem</span>

- Convert data blocks to raid1, skipping already converted chunks (e.g. after a previous cancelled conversion operation):

`sudo btrfs balance start -dconvert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raid1</span>`,soft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_filesystem</span>

- Cancel, pause, or resume a running or paused balance operation:

`sudo btrfs balance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cancel|pause|resume</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_filesystem</span>
