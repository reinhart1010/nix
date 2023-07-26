---
layout: page
title: linux/pw-play (English)
description: "Shorthand tool for pw-cat --playback."
content_hash: 9c15d0c3f3036e98af17accd9fba93e094c3bc9d
last_modified_at: 2023-07-26
related_topics:
  - title: Türkçe version
    url: /tr/linux/pw-play.html
    icon: bi bi-globe
---
# pw-play

Shorthand tool for pw-cat --playback.
More information: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Play a wav sound file over the default target:

`pw-play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Play a wav sound file at a different volume level:

`pw-play --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>
