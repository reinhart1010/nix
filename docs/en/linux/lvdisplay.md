---
layout: page
title: linux/lvdisplay (English)
description: "Display information about Logical Volume Manager (LVM) logical volumes."
content_hash: f0879a7952c74fd325000bf38a9ac007c65eecdc
last_modified_at: 2024-06-18
tldri18n_status: 2
---
# lvdisplay

Display information about Logical Volume Manager (LVM) logical volumes.
See also: `lvm`.
More information: <https://manned.org/lvdisplay>.

- Display information about all logical volumes:

`sudo lvdisplay`

- Display information about all logical volumes in volume group vg1:

`sudo lvdisplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>

- Display information about logical volume lv1 in volume group vg1:

`sudo lvdisplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1/lv1</span>
