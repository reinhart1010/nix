---
layout: page
title: linux/hwinfo (English)
description: "Probe for the hardware present in the system."
content_hash: 9f5f459d27ae8303d75ce9c17a5da6916584f6d6
last_modified_at: 2023-09-28
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># hwinfo

Probe for the hardware present in the system.
More information: <https://manned.org/hwinfo>.

- Get graphics card information:

`hwinfo --gfxcard`

- Get network device information:

`hwinfo --network`

- List disks and CD-ROM drives, abbreviating the output:

`hwinfo --short --disk --cdrom`

- Write all hardware information to a file:

`hwinfo --all --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display help:

`hwinfo --help`
