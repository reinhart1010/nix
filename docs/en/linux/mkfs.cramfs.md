---
layout: page
title: linux/mkfs.cramfs (English)
description: "Creates a ROM filesystem inside a partition."
content_hash: 5e768632a3cca620812ec898141e681b6d545c94
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mkfs.cramfs

Creates a ROM filesystem inside a partition.
More information: <https://manned.org/mkfs.cramfs>.

- Create a ROM filesystem inside partition 1 on device b (`sdb1`):

`mkfs.cramfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create a ROM filesystem with a volume-name:

`mkfs.cramfs -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
