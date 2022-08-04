---
layout: page
title: common/mp4box (English)
description: "MPEG-4 Systems Toolbox - Muxes streams into MP4 container."
content_hash: 95c9b63cdb455f2867a6948321272a55d468ca4b
---
# mp4box

MPEG-4 Systems Toolbox - Muxes streams into MP4 container.
More information: <https://gpac.wp.imt.fr/mp4box>.

- Display information about an existing MP4 file:

`mp4box -info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Add an SRT subtitle file into an MP4 file:

`mp4box -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_subs.srt</span>`:lang=eng -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.mp4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.mp4</span>

- Combine audio from one file and video from another:

`mp4box -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input1.mp4</span>`#audio -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input2.mp4</span>`#video `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.mp4</span>
