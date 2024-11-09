---
layout: page
title: linux/fluidsynth (한국어)
description: "MIDI 파일에서 오디오 합성."
content_hash: fa2a6832a91406f96d6d58f200882f2dfc926ce1
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/fluidsynth.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fluidsynth.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fluidsynth

MIDI 파일에서 오디오 합성.
더 많은 정보: <https://github.com/FluidSynth/fluidsynth/wiki/UserManual>.

- MIDI 파일 재생:

`fluidsynth --audio-driver=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipewire|pulseaudio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사운드폰트.sf2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.midi</span>
