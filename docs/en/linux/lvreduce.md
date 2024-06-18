---
layout: page
title: linux/lvreduce (English)
description: "Reduce the size of a logical volume."
content_hash: 25b2e3620d8eb6746fe1845173a2a4c1fb336b25
last_modified_at: 2024-06-18
tldri18n_status: 2
---
# lvreduce

Reduce the size of a logical volume.
See also: `lvm`.
More information: <https://manned.org/lvreduce>.

- Reduce a volume's size to 120 GB:

`lvreduce --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">120G</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>

- Reduce a volume's size by 40 GB as well as the underlying filesystem:

`lvreduce --size -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40G</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>
