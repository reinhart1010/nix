---
layout: page
title: linux/wf-recorder (English)
description: "Screencast for Wayland optionally with audio."
content_hash: e54d24886e46f738aa7adc9716a36df2392ebaf9
last_modified_at: 2024-12-01
tldri18n_status: 2
---
# wf-recorder

Screencast for Wayland optionally with audio.
By default you need to end the process with Ctrl-C.
More information: <https://github.com/ammen99/wf-recorder>.

- Record storing to an MP4 file:

`wf-recorder --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.mp4</span>

- Record including audio, both with mic and system sounds:

`wf-recorder --audio --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file_with_audio.webm</span>

- Select and record a portion of the screen using `slurp`, outputting to default `recording.mp4`:

`wf-recorder -g "$(slurp)"`
