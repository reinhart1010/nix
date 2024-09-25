---
layout: page
title: linux/mkfs.bcachefs (English)
description: "Create a `bcachefs` filesystem inside a partition."
content_hash: 86cea66ee40fc15c04a8173ffb0400cae5bfbde5
last_modified_at: 2024-09-25
tldri18n_status: 2
---
# mkfs.bcachefs

Create a `bcachefs` filesystem inside a partition.
More information: <https://bcachefs-docs.readthedocs.io/en/latest/mgmt-formatting.html>.

- Create a `bcachefs` filesystem inside partition 1 on a device (`X`):

`sudo mkfs.bcachefs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX1</span>

- Create a `bcachefs` filesystem with a volume label:

`sudo mkfs.bcachefs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-L|--fs_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX1</span>
