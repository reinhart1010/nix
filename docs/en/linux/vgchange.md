---
layout: page
title: linux/vgchange (English)
description: "Change the attributes of a Logical Volume Manager (LVM) volume group."
content_hash: 01a76152160e4610b57c338e695de6f2d59a30f3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# vgchange

Change the attributes of a Logical Volume Manager (LVM) volume group.
See also: `lvm`.
More information: <https://manned.org/vgchange>.

- Change the activation status of logical volumes in all volume groups:

`sudo vgchange --activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y|n</span>

- Change the activation status of logical volumes in the specified volume group (determine with `vgscan`):

`sudo vgchange --activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y|n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_group}</span>
