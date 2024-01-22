---
layout: page
title: linux/rpicam-hello (English)
description: "View a live camera stream using a Raspberry Pi camera."
content_hash: 503d9a3110d3c78d600cf99892e104792ae5eb74
last_modified_at: 2024-01-22
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpicam-hello.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpicam-hello

View a live camera stream using a Raspberry Pi camera.
More information: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-hello>.

- Display a camera preview stream for a specific amount of time (in milliseconds):

`rpicam-hello -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time</span>

- Tune the configuration for a particular camera sensor:

`rpicam-hello --tuning-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/share/libcamera/ipa/rpi/path/to/config.json</span>
