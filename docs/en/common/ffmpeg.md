---
layout: page
title: common/ffmpeg (English)
description: "Video conversion tool."
content_hash: dd100177cb67510ad2d8f8f2d4ed6d12cea5d4c0
last_modified_at: 2023-03-12
related_topics:
  - title: Deutsch version
    url: /de/common/ffmpeg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ffmpeg.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/ffmpeg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ffmpeg.html
    icon: bi bi-globe
---
# ffmpeg

Video conversion tool.
More information: <https://ffmpeg.org>.

- Extract the sound from a video and save it as MP3:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mp4</span>` -vn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sound</span>`.mp3`

- Save a video as GIF, scaling the height to 1000px and setting framerate to 15:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mp4</span>` -vf 'scale=-1:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000</span>`' -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gif</span>

- Combine numbered images (`frame_1.jpg`, `frame_2.jpg`, etc) into a video or GIF:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frame_%d.jpg</span>` -f image2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mpg|video.gif</span>

- Quickly extract a single frame from a video at time mm:ss and save it as a 128x128 resolution image:

`ffmpeg -ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm:ss</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mp4</span>` -frames 1 -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">128x128</span>` -f image2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>

- Trim a video from a given start time mm:ss to an end time mm2:ss2 (omit the -to flag to trim till the end):

`ffmpeg -ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm:ss</span>` -to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm2:ss2</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video.mp4</span>` -codec copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.mp4</span>

- Convert AVI video to MP4. AAC Audio @ 128kbit, h264 Video @ CRF 23:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_video</span>`.avi -codec:a aac -b:a 128k -codec:v libx264 -crf 23 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_video</span>`.mp4`

- Remux MKV video to MP4 without re-encoding audio or video streams:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_video</span>`.mkv -codec copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_video</span>`.mp4`

- Convert MP4 video to VP9 codec. For the best quality, use a CRF value (recommended range 15-35) and -b:v MUST be 0:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_video</span>`.mp4 -codec:v libvpx-vp9 -crf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` -b:v 0 -codec:a libopus -vbr on -threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_threads</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_video</span>`.webm`
