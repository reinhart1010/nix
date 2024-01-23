---
layout: page
title: linux/rpicam-jpeg (English)
description: "Capture and store a JPEG image using a Raspberry Pi camera."
content_hash: e14e3048533754f54b56ce718815ff4f1e813272
last_modified_at: 2024-01-23
tldri18n_status: 2
---
# rpicam-jpeg

Capture and store a JPEG image using a Raspberry Pi camera.
More information: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-jpeg>.

- Capture an image and name the file:

`rpicam-jpeg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>

- Capture an image with set dimensions:

`rpicam-jpeg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>` --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920</span>` --height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1080</span>

- Capture an image with an exposure of 20 seconds and a gain of 150%:

`rpicam-jpeg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>` --shutter 20000 --gain 1.5`
