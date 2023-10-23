---
layout: page
title: linux/pw-play (English)
description: "Record audio files through pipewire."
content_hash: d594150f5b4075ea5d85cf9e840e21dedeab970e
last_modified_at: 2023-10-23
related_topics:
  - title: Türkçe version
    url: /tr/linux/pw-play.html
    icon: bi bi-globe
---
# pw-play

Record audio files through pipewire.
Shorthand for pw-cat --playback.
More information: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Play a wav sound file over the default target:

`pw-play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Play a wav sound file at a different volume level:

`pw-play --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>
