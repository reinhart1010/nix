---
layout: page
title: linux/zbarcam (English)
description: "Scans and decodes barcodes (and QR codes) from a video device."
content_hash: bb1b60e4db4adba9bcab028b29c112de627844a6
last_modified_at: 2023-07-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zbarcam

Scans and decodes barcodes (and QR codes) from a video device.
More information: <https://manned.org/zbarcam>.

- Continuously read barcodes and print them to standard output:

`zbarcam`

- Disable output video window while scanning:

`zbarcam --nodisplay`

- Print barcodes without type information:

`zbarcam --raw`

- Define capture device:

`zbarcam /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video_device</span>
