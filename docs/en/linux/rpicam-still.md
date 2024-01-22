---
layout: page
title: linux/rpicam-still (English)
description: "Capture and store a photo using a Raspberry Pi camera with legacy features missing from `rpicam-jpeg`."
content_hash: 1657dbd8e79e2d38e8ab4630bb3127874996a60b
last_modified_at: 2024-01-22
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpicam-still.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpicam-still

Capture and store a photo using a Raspberry Pi camera with legacy features missing from `rpicam-jpeg`.
More information: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-still>.

- Capture a photo with different encoding:

`rpicam-still -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bmp|png|rgb|yuv420</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bmp|png|rgb|yuv420}</span>`}`

- Capture a raw image:

`rpicam-still -r -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>

- Capture a 100 second exposure image:

`rpicam-still -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>` --shutter 100000`
