---
layout: page
title: linux/pw-play (English)
description: "Play audio files through `pipewire`."
content_hash: f48b59e23bdcdf2ffb1847f9c41319fbcc5f2ce4
last_modified_at: 2024-01-08
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-play.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-play.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-play

Play audio files through `pipewire`.
Shorthand for `pw-cat --playback`.
More information: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Play a WAV sound file over the default target:

`pw-play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Play a WAV sound file at a different volume level:

`pw-play --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>
