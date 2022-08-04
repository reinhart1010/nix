---
layout: page
title: linux/e2fsck (English)
description: "Check a Linux ext2/ext3/ext4 filesystem. The filesystem should be unmounted at the time the command is run."
content_hash: ab76e62a416662577ffbfbe76774329315387f60
---
# e2fsck

Check a Linux ext2/ext3/ext4 filesystem. The filesystem should be unmounted at the time the command is run.
More information: <https://manned.org/e2fsck>.

- Check filesystem, reporting any damaged blocks:

`e2fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Check filesystem and automatically repair any damaged blocks:

`e2fsck -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Check filesystem in read only mode:

`e2fsck -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
