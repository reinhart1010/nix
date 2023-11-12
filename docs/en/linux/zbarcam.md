---
layout: page
title: linux/zbarcam (English)
description: "Scan and decode barcodes (and QR codes) from a video device."
content_hash: 5af1e79dbc28782a6ffcfe9bd5da90fe3e3c3609
last_modified_at: 2023-11-12
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

`zbarcam /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video_device</span>
