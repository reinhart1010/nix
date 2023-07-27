---
layout: page
title: common/gst-launch-1.0 (English)
description: "Build and run a GStreamer pipeline."
content_hash: 7915f593812c095003b1db0c3d64c249b1ce2e0a
last_modified_at: 2023-07-27
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gst-launch-1.0

Build and run a GStreamer pipeline.
More information: <https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html?gi-language=c>.

- Play test video in a window:

`gst-launch-1.0 videotestsrc ! xvimagesink`

- Play a media file in a window:

`gst-launch-1.0 playbin uri=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocol</span>`://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Re-encode a media file:

`gst-launch-1.0 filesrc location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` ! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_type</span>`demux ! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codec_type</span>`dec ! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codec_type</span>`enc ! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_type</span>`mux ! filesink location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Stream a file to an RTSP server:

`gst-launch-1.0 filesrc location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` ! rtspclientsink location=rtsp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_IP</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
