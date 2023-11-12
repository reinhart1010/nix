---
layout: page
title: common/handbrakecli (English)
description: "Command-line interface to the HandBrake video conversion and DVD ripping tool."
content_hash: 3458ad5ff2a670d96ab3ac31ba11402552479195
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# handbrakecli

Command-line interface to the HandBrake video conversion and DVD ripping tool.
More information: <https://handbrake.fr/>.

- Convert a video file to MKV (AAC 160kbit audio and x264 CRF20 video):

`handbrakecli --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.avi</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.mkv</span>` --encoder x264 --quality 20 --ab 160`

- Resize a video file to 320x240:

`handbrakecli --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.mp4</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.mp4</span>` --width 320 --height 240`

- List available presets:

`handbrakecli --preset-list`

- Convert an AVI video to MP4 using the Android preset:

`handbrakecli --preset="Android" --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.ext</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.mp4</span>

- Print the content of a DVD, getting the CSS keys in the process:

`handbrakecli --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sr0</span>` --title 0`

- Rip the first track of a DVD in the specified device. Audiotracks and subtitle languages are specified as lists:

`handbrakecli --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sr0</span>` --title 1 --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">out.mkv</span>` --format av_mkv --encoder x264 --subtitle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,4,5</span>` --audio `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,2</span>` --aencoder copy --quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">23</span>
