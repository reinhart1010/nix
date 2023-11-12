---
layout: page
title: linux/lvresize (English)
description: "Change the size of a logical volume."
content_hash: c540bd35e41a7c5dbbc798bee2ae6b4cc17fed8d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lvresize

Change the size of a logical volume.
See also: `lvm`.
More information: <https://man7.org/linux/man-pages/man8/lvresize.8.html>.

- Change the size of a logical volume to 120 GB:

`lvresize --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">120G</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>

- Extend the size of a logical volume as well as the underlying filesystem by 120 GB:

`lvresize --size +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">120G</span>` --resizefs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>

- Extend the size of a logical volume to 100% of the free physical volume space:

`lvresize --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>`%FREE `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>

- Reduce the size of a logical volume as well as the underlying filesystem by 120 GB:

`lvresize --size -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">120G</span>` --resizefs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>
