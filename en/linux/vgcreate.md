---
layout: page
title: linux/vgcreate (English)
description: "Create volume groups combining multiple mass-storage devices."
content_hash: d819028d284f72e03960378d9f7756d523507106
---
# vgcreate

Create volume groups combining multiple mass-storage devices.
See also: `lvm`.
More information: <https://man7.org/linux/man-pages/man8/vgcreate.8.html>.

- Create a new volume group called vg1 using the `/dev/sda1` device:

`vgcreate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- Create a new volume group called vg1 using multiple devices:

`vgcreate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdc1</span>
