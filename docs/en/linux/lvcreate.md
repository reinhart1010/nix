---
layout: page
title: linux/lvcreate (English)
description: "Create a logical volume in an existing volume group. A volume group is a collection of logical and physical volumes."
content_hash: 39e2449ddb32d5fb2b7c9f3825a4e2981f01d58a
last_modified_at: 2024-06-18
tldri18n_status: 2
---
# lvcreate

Create a logical volume in an existing volume group. A volume group is a collection of logical and physical volumes.
See also: `lvm`.
More information: <https://manned.org/lvcreate>.

- Create a logical volume of 10 gigabytes in the volume group vg1:

`lvcreate -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10G</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>

- Create a 1500 megabyte linear logical volume named mylv in the volume group vg1:

`lvcreate -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1500</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mylv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>

- Create a logical volume called mylv that uses 60% of the total space in volume group vg1:

`lvcreate -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60%VG</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mylv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>

- Create a logical volume called mylv that uses all the unallocated space in the volume group vg1:

`lvcreate -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100%FREE</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mylv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>
