---
layout: page
title: linux/blockdev (English)
description: "Manage, query, and manipulate block devices."
content_hash: 663d529551121114cfee4b30a59821d101b252b2
last_modified_at: 2024-10-06
tldri18n_status: 2
---
# blockdev

Manage, query, and manipulate block devices.
More information: <https://manned.org/blockdev>.

- Print a report for all devices:

`sudo blockdev --report`

- Print a report for a specific device:

`sudo blockdev --report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Get the size of a device in 512-byte sectors:

`sudo blockdev --getsz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Set read-only:

`sudo blockdev --setro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Set read-write:

`sudo blockdev --setrw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Flush buffers:

`sudo blockdev --flushbufs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Get the physical block size:

`sudo blockdev --getpbsz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Set the read-ahead value to 128 sectors:

`sudo blockdev --setra 128 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>
