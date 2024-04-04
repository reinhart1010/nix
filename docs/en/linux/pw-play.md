---
layout: page
title: linux/pw-play (English)
description: "Play audio files through PipeWire."
content_hash: 5931ba44fae6f960f4598a237396aa9155aa9f3d
last_modified_at: 2024-04-04
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

Play audio files through PipeWire.
Shorthand for `pw-cat --playback`.
See also: `play`.
More information: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Play a WAV sound file over the default target:

`pw-play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Play a WAV sound file at a different volume level:

`pw-play --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>
