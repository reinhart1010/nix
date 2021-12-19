---
layout: page
title: linux/pw-cat (English)
description: "Pipewire tool for playing and recording audio files."
content_hash: fda764d6867553ec753c9e381b66f44fcac8c577
---
# pw-cat

Pipewire tool for playing and recording audio files.
More information: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- List all available playback targets:

`pw-cat --playback --list-targets`

- Play a WAV file over the default target:

`pw-cat --playback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- List all available record targets:

`pw-cat --record --list-targets`

- Record a sample recording at a different volume level:

`pw-cat --record --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Record a sample recording using a different sample rate:

`pw-cat --record --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>
