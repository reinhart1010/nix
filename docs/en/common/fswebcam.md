---
layout: page
title: common/fswebcam (English)
description: "Small and simple webcam for *nix."
content_hash: 1b03f1f233b7b32909618102ce36a0d47184dff2
---
# fswebcam

Small and simple webcam for *nix.
More information: <https://www.sanslogic.co.uk/fswebcam>.

- Take a picture:

`fswebcam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Take a picture with custom resolution:

`fswebcam -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Take a picture from selected device(Default is `/dev/video0`):

`fswebcam -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Take a picture with timestamp(timestamp string is formatted by strftime):

`fswebcam --timestamp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timestamp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>
