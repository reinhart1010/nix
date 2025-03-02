---
layout: page
title: linux/pw-play (한국어)
description: "PipeWire를 통해 오디오 파일 재생."
content_hash: 4a37c5eefbcdad9039624f32c332b5d3bc9f2a2e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/pw-play.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/pw-play.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-play.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-play.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pw-play

PipeWire를 통해 오디오 파일 재생.
`pw-cat --playback`의 약어.
같이 보기: `play`.
더 많은 정보: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- 기본 대상에서 WAV 사운드 파일 재생:

`pw-play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>

- 다른 볼륨 수준으로 WAV 사운드 파일 재생:

`pw-play --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>
