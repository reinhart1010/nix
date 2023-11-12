---
layout: page
title: common/opusenc (italiano)
description: "Converte audio WAV o FLAC in Opus."
content_hash: 07249c78d29b6d7eae9730519aec7f4453b1c1c7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/opusenc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# opusenc

Converte audio WAV o FLAC in Opus.
Maggiori informazioni: <https://opus-codec.org/docs/opus-tools/opusenc.html>.

- Converte un file WAV in un file Opus usando le opzioni predefinite:

`opusenc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_originale.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_convertito</span>`.opus`

- Converte un audio stereo alla massima qualità possibile:

`opusenc --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_originale.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_convertito</span>`.opus`

- Converte un audio con canali surround 5.1 alla massima qualità possibile:

`opusenc --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1536</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_originale.flac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_convertito</span>`.opus`

- Converte l'audio di una voce alla minima qualità possibile:

`opusenc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_originale.wav</span>` --downmix-mono --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_convertito</span>`.opus`
