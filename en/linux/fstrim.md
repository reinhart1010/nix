---
layout: page
title: linux/fstrim (English)
description: "Discard unused blocks on a mounted filesystem."
content_hash: e607e0bd2d287f32283095cd39389c3bd6f53015
---
# fstrim

Discard unused blocks on a mounted filesystem.
Only supported by flash memory devices such as SSDs and microSD cards.
More information: <https://manned.org/fstrim>.

- Trim unused blocks on all mounted partitions that support it:

`sudo fstrim --all`

- Trim unused blocks on a specified partition:

`sudo fstrim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/</span>

- Display statistics after trimming:

`sudo fstrim --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/</span>
