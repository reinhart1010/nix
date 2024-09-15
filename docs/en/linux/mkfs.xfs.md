---
layout: page
title: linux/mkfs.xfs (English)
description: "Create an XFS filesystem inside a partition."
content_hash: 01ccfad9da4ac05a13f712b60cde7528b329428f
last_modified_at: 2024-09-15
tldri18n_status: 2
---
# mkfs.xfs

Create an XFS filesystem inside a partition.
More information: <https://manned.org/mkfs.xfs>.

- Create an XFS filesystem inside partition 1 on a device (`X`):

`sudo mkfs.xfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX1</span>

- Create an XFS filesystem with a volume label:

`sudo mkfs.xfs -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX1</span>
