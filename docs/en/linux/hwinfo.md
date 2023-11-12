---
layout: page
title: linux/hwinfo (English)
description: "Probe for the hardware present in the system."
content_hash: b6794b8f8f56addd861f83219e891633a41ce05f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# hwinfo

Probe for the hardware present in the system.
More information: <https://manpages.opensuse.org/hwinfo/hwinfo.8.en.html>.

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
