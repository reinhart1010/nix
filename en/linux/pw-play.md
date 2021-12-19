---
layout: page
title: linux/pw-play (English)
description: "Shorthand tool for pw-cat --playback."
content_hash: 27edcdf734c9aa7aeb92bc12e2832300ad14828d
---
# pw-play

Shorthand tool for pw-cat --playback.
More information: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- List all available playback targets:

`pw-play --list-targets`

- Play a wav sound file over the default target:

`pw-play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Play a wav sound file at a different volume level:

`pw-play --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>
