---
layout: page
title: linux/rpicam-vid (English)
description: "Capture a video using a Raspberry Pi camera."
content_hash: 10d2e39cbd2af86017ee22988f68411aea88c43e
last_modified_at: 2024-01-23
tldri18n_status: 2
---
# rpicam-vid

Capture a video using a Raspberry Pi camera.
Some subcommands such as `vlc` have their own usage documentation.
More information: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-vid>.

- Capture a 10 second video:

`rpicam-vid -t 10000 -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.h264</span>

- Play the video using `vlc`:

`vlc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.h264</span>
