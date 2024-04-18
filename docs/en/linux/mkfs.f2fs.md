---
layout: page
title: linux/mkfs.f2fs (English)
description: "Create an F2FS filesystem inside a partition."
content_hash: 0b2aa4817d832d4bdc08291f11099c097967d156
last_modified_at: 2024-04-18
related_topics:
  - title: español version
    url: /es/linux/mkfs.f2fs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.f2fs

Create an F2FS filesystem inside a partition.
More information: <https://manned.org/mkfs.f2fs>.

- Create an F2FS filesystem inside partition 1 on device b (`sdb1`):

`sudo mkfs.f2fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create an F2FS filesystem with a volume label:

`sudo mkfs.f2fs -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
