---
layout: page
title: common/mpv (English)
description: "A audio/video player based on MPlayer."
content_hash: 8c22a5ec465ff8d82465b37ee701ec3345149963
last_modified_at: 2024-06-04
related_topics:
  - title: italiano version
    url: /it/common/mpv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mpv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mpv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mpv

A audio/video player based on MPlayer.
See also: `mplayer`, `vlc`.
More information: <https://mpv.io>.

- Play a video or audio from a URL or file:

`mpv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>`'`

- Jump backward/forward 5 seconds:

`LEFT <or> RIGHT`

- Jump backward/forward 1 minute:

`DOWN <or> UP`

- Decrease or increase playback speed by 10%:

`[ <or> ]`

- Take a screenshot of the current frame (saved to `./mpv-shotNNNN.jpg` by default):

`s`

- Play a file at a specified speed (1 by default):

`mpv --speed=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.01..100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Play a file using a profile defined in the `mpv.conf` file:

`mpv --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display the output of webcam or other video input device:

`mpv /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video0</span>
