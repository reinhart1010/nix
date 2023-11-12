---
layout: page
title: linux/lvextend (English)
description: "Increase the size of a logical volume."
content_hash: fe91c39a2f4dc1262607136af65c23790243ff3a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lvextend

Increase the size of a logical volume.
See also: `lvm`.
More information: <https://man7.org/linux/man-pages/man8/lvextend.8.html>.

- Increase a volume's size to 120 GB:

`lvextend --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">120G</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>

- Increase a volume's size by 40 GB as well as the underlying filesystem:

`lvextend --size +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40G</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>

- Increase a volume's size to 100% of the free physical volume space:

`lvextend --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>`%FREE `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>
