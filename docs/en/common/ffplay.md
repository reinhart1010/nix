---
layout: page
title: common/ffplay (English)
description: "A simple and portable media player using the FFmpeg libraries and the SDL library."
content_hash: f71f9b9f413cb2e333768abfdeb9f1116623fb0a
---
# ffplay

A simple and portable media player using the FFmpeg libraries and the SDL library.
More information: <https://ffmpeg.org/ffplay-all.html>.

- Play a media file:

`ffplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Play a video and show motion vectors in real time:

`ffplay -flags2 +export_mvs -vf codecview=mv=pf+bf+bb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show only video keyframes:

`ffplay -vf select="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eq(pict_type\,PICT_TYPE_I)</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
