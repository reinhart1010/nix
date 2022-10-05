---
layout: page
title: linux/e2fsck (English)
description: "Check a Linux ext2/ext3/ext4 filesystem. The partition should be unmounted."
content_hash: b946d4eb9780908301cf849ee82b89032eff0520
---
# e2fsck

Check a Linux ext2/ext3/ext4 filesystem. The partition should be unmounted.
More information: <https://manned.org/e2fsck>.

- Check filesystem, reporting any damaged blocks:

`sudo e2fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Check filesystem and automatically repair any damaged blocks:

`sudo e2fsck -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Check filesystem in read only mode:

`sudo e2fsck -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Perform an exhaustive, non-destructive read-write test for bad blocks and blacklist them:

`sudo e2fsck -fccky `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
