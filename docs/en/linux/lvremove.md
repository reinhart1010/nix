---
layout: page
title: linux/lvremove (English)
description: "Remove logical volumes."
content_hash: 8bb62d7708da17f8ae4314a5ae900c2b10468a38
last_modified_at: 2024-06-20
tldri18n_status: 2
---
# lvremove

Remove logical volumes.
See also: `lvm`.
More information: <https://manned.org/lvremove>.

- Remove a logical volume in a volume group:

`sudo lvremove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>

- Remove all logical volumes in a volume group:

`sudo lvremove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>
