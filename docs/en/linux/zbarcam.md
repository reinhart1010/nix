---
layout: page
title: linux/zbarcam (English)
description: "Scan and decode barcodes (and QR codes) from a video device."
content_hash: e58eeab970f8a74ffecccdb10d8ba142b805a6cb
last_modified_at: 2024-06-11
tldri18n_status: 2
---
# zbarcam

Scan and decode barcodes (and QR codes) from a video device.
More information: <https://manned.org/zbarcam>.

- Continuously read barcodes and print them to `stdout`:

`zbarcam`

- Disable output video window while scanning:

`zbarcam --nodisplay`

- Print barcodes without type information:

`zbarcam --raw`

- Define capture device:

`zbarcam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/video_device</span>
