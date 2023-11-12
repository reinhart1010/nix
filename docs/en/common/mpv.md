---
layout: page
title: common/mpv (English)
description: "A audio/video player based on MPlayer."
content_hash: 50e3ddcc1b9feb01bb42d8044b56efd3443c1565
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/mpv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mpv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mpv

A audio/video player based on MPlayer.
More information: <https://mpv.io>.

- Play a video or audio file:

`mpv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Play a video or audio file from a URL:

`mpv '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=dQw4w9WgXcQ</span>`'`

- Jump backward/forward 5 seconds:

`LEFT <or> RIGHT`

- Jump backward/forward 1 minute:

`DOWN <or> UP`

- Decrease or increase playback speed by 10%:

`[ <or> ]`

- Play a file at a specified speed (0.01 to 100, default 1):

`mpv --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">speed</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Play a file using a profile defined in the `mpv.conf` file:

`mpv --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display the output of webcam or other video input device:

`mpv /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video0</span>
