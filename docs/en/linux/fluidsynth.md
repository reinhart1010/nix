---
layout: page
title: linux/fluidsynth (English)
description: "Synthesize audio from MIDI files."
content_hash: 5f05ddce052160b92e09d81a74379b795eeaecf6
last_modified_at: 2023-08-08
---
# fluidsynth

Synthesize audio from MIDI files.
More information: <https://github.com/FluidSynth/fluidsynth/wiki/UserManual>.

- Play a MIDI file:

`fluidsynth --audio-driver=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipewire|pulseaudio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/soundfont.sf2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.midi</span>
