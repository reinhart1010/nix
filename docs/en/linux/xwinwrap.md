---
layout: page
title: linux/xwinwrap (English)
description: "Run a player or a program as desktop background."
content_hash: 4bbf035cc1be618b55fbb8a95d37b1ddc557a953
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/xwinwrap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xwinwrap

Run a player or a program as desktop background.
More information: <https://github.com/ujjwal96/xwinwrap>.

- Run a video using mpv:

`xwinwrap -b -nf -ov -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv</span>` -wid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wid</span>` --loop --no-audio --no-resume-playback --panscan=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/video.mp4</span>

- Run a video in fullscreen using mpv:

`xwinwrap -b -nf -fs -ov -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv</span>` -wid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wid</span>` --loop --no-audio --no-resume-playback --panscan=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/video.mp4</span>

- Run a video using mpv with 80% opacity:

`xwinwrap -b -nf -ov -o 0.8 --- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv</span>` -wid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wid</span>` --loop --no-audio --no-resume-playback --panscan=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/video.mp4</span>

- Run a video using mpv in a second monitor 1600x900 with 1920 offset on X-axis:

`xwinwrap -g 1600x900+1920 -b -nf -ov -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv</span>` -wid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wid</span>` --loop --no-audio --no-resume-playback --panscan=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/video.mkv</span>
