---
layout: page
title: linux/rpicam-jpeg (English)
description: "Capture and store a JPEG image using a Raspberry Pi camera."
content_hash: e14e3048533754f54b56ce718815ff4f1e813272
last_modified_at: 2024-01-22
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpicam-jpeg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpicam-jpeg

Capture and store a JPEG image using a Raspberry Pi camera.
More information: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-jpeg>.

- Capture an image and name the file:

`rpicam-jpeg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>

- Capture an image with set dimensions:

`rpicam-jpeg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>` --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920</span>` --height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1080</span>

- Capture an image with an exposure of 20 seconds and a gain of 150%:

`rpicam-jpeg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>` --shutter 20000 --gain 1.5`
