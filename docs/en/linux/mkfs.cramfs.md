---
layout: page
title: linux/mkfs.cramfs (English)
description: "Create a ROM filesystem inside a partition."
content_hash: 97438b2a5992cac13670b7d5919fc42fea9d7e72
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# mkfs.cramfs

Create a ROM filesystem inside a partition.
More information: <https://manned.org/mkfs.cramfs>.

- Create a ROM filesystem inside partition 1 on device b (`sdb1`):

`mkfs.cramfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create a ROM filesystem with a volume-name:

`mkfs.cramfs -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
