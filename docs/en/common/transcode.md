---
layout: page
title: common/transcode (English)
description: "Transcode video and audio codecs, and convert between media formats."
content_hash: 7e14bbd3c73f52f2d2d8527047726651de75303e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# transcode

Transcode video and audio codecs, and convert between media formats.
More information: <https://manned.org/transcode>.

- Create stabilization file to be able to remove camera shakes:

`transcode -J stabilize -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Remove camera shakes after creating stabilization file, transform video using XviD:

`transcode -J transform -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>` -y xvid -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>

- Resize the video to 640x480 pixels and convert to MPEG4 codec using XviD:

`transcode -Z 640x480 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>` -y xvid -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>
