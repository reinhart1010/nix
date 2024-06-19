---
layout: page
title: linux/vgcreate (English)
description: "Create volume groups combining multiple mass-storage devices."
content_hash: c1995303b40b5c37c8b2546d3896de5327023ec8
last_modified_at: 2024-06-19
tldri18n_status: 2
---
# vgcreate

Create volume groups combining multiple mass-storage devices.
See also: `lvm`.
More information: <https://manned.org/vgcreate>.

- Create a new volume group called vg1 using the `/dev/sda1` device:

`vgcreate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- Create a new volume group called vg1 using multiple devices:

`vgcreate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdc1</span>
