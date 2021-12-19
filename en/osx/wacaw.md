---
layout: page
title: osx/wacaw (English)
description: "A little command-line tool for macOS that allows you to capture both still pictures and video from an attached camera."
content_hash: 325266f88f771ee841ac436afaacef77ab7f5584
related_topics:
  - title: 中文 version
    url: /zh/osx/wacaw.html
    icon: bi bi-globe
---
# wacaw

A little command-line tool for macOS that allows you to capture both still pictures and video from an attached camera.
More information: <http://webcam-tools.sourceforge.net>.

- Take a picture from webcam:

`wacaw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Record a video:

`wacaw --video `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duration_in_seconds</span>

- Take a picture with custom resolution:

`wacaw -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Copy image just taken to clipboard:

`wacaw --to-clipboard`

- List the devices available:

`wacaw -L`
