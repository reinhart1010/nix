---
layout: page
title: common/mp4box (English)
description: "MPEG-4 Systems Toolbox: muxe streams into MP4 container."
content_hash: 44335c552150347068e8f36cfa3cd67f4c3782e5
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# mp4box

MPEG-4 Systems Toolbox: muxe streams into MP4 container.
More information: <https://gpac.wp.imt.fr/mp4box>.

- Display information about an existing MP4 file:

`mp4box -info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Add an SRT subtitle file into an MP4 file:

`mp4box -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_subs.srt</span>`:lang=eng -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.mp4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.mp4</span>

- Combine audio from one file and video from another:

`mp4box -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input1.mp4</span>`#audio -add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input2.mp4</span>`#video `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.mp4</span>
