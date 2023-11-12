---
layout: page
title: linux/arecord (English)
description: "Sound recorder for ALSA soundcard driver."
content_hash: 7117ccc5fe1d7a7352e2db1cb2ab56d30c1b3209
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/arecord.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arecord.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arecord

Sound recorder for ALSA soundcard driver.
More information: <https://manned.org/arecord>.

- Record a snippet in "CD" quality (finish with Ctrl-C when done):

`arecord -vv --format=cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Record a snippet in "CD" quality, with a fixed duration of 10 seconds:

`arecord -vv --format=cd --duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Record a snippet and save it as an MP3 (finish with Ctrl-C when done):

`arecord -vv --format=cd --file-type raw | lame -r - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mp3</span>

- List all sound cards and digital audio devices:

`arecord --list-devices`

- Allow interactive interface (e.g. use space-bar or enter to play or pause):

`arecord --interactive`
