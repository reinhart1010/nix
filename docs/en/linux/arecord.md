---
layout: page
title: linux/arecord (English)
description: "Sound recorder for ALSA soundcard driver."
content_hash: 9a7a9e96c2d2c15e7678dc1f1ac48ac671408d27
last_modified_at: 2024-05-20
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

- Test your microphone by recording a 5 second sample and playing it back:

`arecord -d 5 test-mic.wav && aplay test-mic.wav && rm test-mic.wav`
