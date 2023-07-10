---
layout: page
title: common/ffplay (English)
description: "A simple and portable media player using the FFmpeg libraries and the SDL library."
content_hash: 0e696f4899fda903875970aa3eb4e00834475eb4
last_modified_at: 2023-07-10
---
# ffplay

A simple and portable media player using the FFmpeg libraries and the SDL library.
More information: <https://ffmpeg.org/ffplay-all.html>.

- Play a media file:

`ffplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Play audio from a media file without a GUI:

`ffplay -nodisp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Play media passed by `ffmpeg` through `stdin`:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">copy</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media_format</span>` - | ffplay -`

- Play a video and show motion vectors in real time:

`ffplay -flags2 +export_mvs -vf codecview=mv=pf+bf+bb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show only video keyframes:

`ffplay -vf select="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eq(pict_type\,PICT_TYPE_I)</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
