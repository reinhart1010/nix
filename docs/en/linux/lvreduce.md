---
layout: page
title: linux/lvreduce (English)
description: "Reduce the size of a logical volume."
content_hash: e408aa97a9eb98628652cc1edc42a91eabec96cf
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lvreduce

Reduce the size of a logical volume.
See also: `lvm`.
More information: <https://man7.org/linux/man-pages/man8/lvreduce.8.html>.

- Reduce a volume's size to 120 GB:

`lvreduce --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">120G</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>

- Reduce a volume's size by 40 GB as well as the underlying filesystem:

`lvreduce --size -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40G</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>
