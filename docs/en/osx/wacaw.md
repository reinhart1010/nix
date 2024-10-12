---
layout: page
title: osx/wacaw (English)
description: "Capture both still pictures and video from an attached camera."
content_hash: 7e8f0f936ece8e02f8be8b8b7b0decdf12b62e53
last_modified_at: 2024-10-12
related_topics:
  - title: español version
    url: /es/osx/wacaw.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/wacaw.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wacaw

Capture both still pictures and video from an attached camera.
More information: <https://webcam-tools.sourceforge.net>.

- Take a picture from webcam:

`wacaw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Record a video:

`wacaw --video `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` --duration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Take a picture with custom resolution:

`wacaw --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` --height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Copy image just taken to clipboard:

`wacaw --to-clipboard`

- List the devices available:

`wacaw --list-devices`
