---
layout: page
title: linux/lvremove (English)
description: "Remove logical volumes."
content_hash: 9b77f8b4b7dfb40eb3e77d90d9a300af1f0f797b
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# lvremove

Remove logical volumes.
See also: `lvm`.
More information: <https://man7.org/linux/man-pages/man8/lvremove.8.html>.

- Remove a logical volume in a volume group:

`sudo lvremove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logical_volume</span>

- Remove all logical volumes in a volume group:

`sudo lvremove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group</span>
