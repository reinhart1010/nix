---
layout: page
title: common/timidity (English)
description: "Play and convert MIDI files."
content_hash: 64ca615f63de60edba5ac9c59afe6162740673f2
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# timidity

Play and convert MIDI files.
More information: <https://timidity.sourceforge.net>.

- Play a MIDI file:

`timidity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mid</span>

- Play a MIDI file in a loop:

`timidity --loop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mid</span>

- Play a MIDI file in a specific key (0 = C major/A minor, -1 = F major/D minor, +1 = G major/E minor, etc.):

`timidity --force-keysig=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-flats|+sharps</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mid</span>

- Convert a MIDI file to PCM (WAV) audio:

`timidity --output-mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">w</span>` --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mid</span>

- Convert a MIDI file to FLAC audio:

`timidity --output-mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">F</span>` --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.flac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mid</span>
