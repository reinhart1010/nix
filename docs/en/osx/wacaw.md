---
layout: page
title: osx/wacaw (English)
description: "Command-line tool for macOS to capture both still pictures and video from an attached camera."
content_hash: 5ea521b0d46e8fac86d42d4f7d3f2abfa61e86d2
last_modified_at: 2023-11-12
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

Command-line tool for macOS to capture both still pictures and video from an attached camera.
More information: <http://webcam-tools.sourceforge.net>.

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
