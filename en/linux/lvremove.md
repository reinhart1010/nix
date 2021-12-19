---
layout: page
title: linux/lvremove (English)
description: "Remove one or more logical volumes."
content_hash: 62d270a9ab7a4a292b2c742d03ed62c140010677
---
# lvremove

Remove one or more logical volumes.
See also: `lvm`.
More information: <https://man7.org/linux/man-pages/man8/lvremove.8.html>.

- Remove a logical volume in a volume group:

`sudo lvremove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>

- Remove all logical volumes in a volume group:

`sudo lvremove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>
