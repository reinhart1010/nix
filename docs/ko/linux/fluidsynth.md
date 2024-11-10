---
layout: page
title: linux/fluidsynth (한국어)
description: "MIDI 파일에서 오디오 합성."
content_hash: fa2a6832a91406f96d6d58f200882f2dfc926ce1
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/fluidsynth.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fluidsynth

MIDI 파일에서 오디오 합성.
더 많은 정보: <https://github.com/FluidSynth/fluidsynth/wiki/UserManual>.

- MIDI 파일 재생:

`fluidsynth --audio-driver=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipewire|pulseaudio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사운드폰트.sf2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.midi</span>
