---
layout: page
title: linux/rpicam-raw (English)
description: "Capture a raw video on a Raspberry Pi camera."
content_hash: 1a49dfab46f3f938f5f70fd7ee22b6f7bddbb53d
last_modified_at: 2024-11-09
tldri18n_status: 2
---
# rpicam-raw

Capture a raw video on a Raspberry Pi camera.
More information: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-raw>.

- Capture a video for a specific amount of seconds:

`rpicam-raw -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2000</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.raw</span>

- Change video dimensions and framerate:

`rpicam-raw -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>` --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4056</span>` --height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3040</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.raw</span>` --framerate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>
