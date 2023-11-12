---
layout: page
title: linux/lvdisplay (English)
description: "Display information about Logical Volume Manager (LVM) logical volumes."
content_hash: 6da60533d3896c898a3d3d23442e87a10f574920
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lvdisplay

Display information about Logical Volume Manager (LVM) logical volumes.
See also: `lvm`.
More information: <https://man7.org/linux/man-pages/man8/lvdisplay.8.html>.

- Display information about all logical volumes:

`sudo lvdisplay`

- Display information about all logical volumes in volume group vg1:

`sudo lvdisplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>

- Display information about logical volume lv1 in volume group vg1:

`sudo lvdisplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1/lv1</span>
