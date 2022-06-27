---
layout: page
title: linux/dumpe2fs (English)
description: "Print the super block and blocks group information for ext2/ext3/ext4 filesystems."
content_hash: fefac5a8ebf52af18df5c52f7e0e207b252ce8be
---
# dumpe2fs

Print the super block and blocks group information for ext2/ext3/ext4 filesystems.
Unmount the partition before running this command using `umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>.
More information: <https://manned.org/dumpe2fs>.

- Display ext2, ext3 and ext4 filesystem information:

`dumpe2fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Display the blocks which are reserved as bad in the filesystem:

`dumpe2fs -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Force display filesystem information even with unrecognizable feature flags:

`dumpe2fs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Only display the superblock information and not any of the block group descriptor detail information:

`dumpe2fs -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Print the detailed group information block numbers in hexadecimal format:

`dumpe2fs -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
