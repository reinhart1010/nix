---
layout: page
title: common/ffprobe (English)
description: "Multimedia stream analyzer."
content_hash: cc0e90f91a590c56d079b8ddf5c1a218523d6b56
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ffprobe.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ffprobe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ffprobe

Multimedia stream analyzer.
More information: <https://ffmpeg.org/ffprobe.html>.

- Display all available stream info for a media file:

`ffprobe -v error -show_streams `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.mp4</span>

- Display media duration:

`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.mp4</span>

- Display the frame rate of a video:

`ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.mp4</span>

- Display the width or height of a video:

`ffprobe -v error -select_streams v:0 -show_entries stream=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width|height</span>` -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.mp4</span>

- Display the average bit rate of a video:

`ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.mp4</span>
