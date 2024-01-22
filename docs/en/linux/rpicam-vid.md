---
layout: page
title: linux/rpicam-vid (English)
description: "Capture a video using a Raspberry Pi camera."
content_hash: 10d2e39cbd2af86017ee22988f68411aea88c43e
last_modified_at: 2024-01-22
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpicam-vid.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpicam-vid

Capture a video using a Raspberry Pi camera.
Some subcommands such as `vlc` have their own usage documentation.
More information: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-vid>.

- Capture a 10 second video:

`rpicam-vid -t 10000 -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.h264</span>

- Play the video using `vlc`:

`vlc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.h264</span>
