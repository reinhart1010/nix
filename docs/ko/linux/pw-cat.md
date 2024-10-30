---
layout: page
title: linux/pw-cat (한국어)
description: "PipeWire를 통해 오디오 파일을 재생하고 녹음."
content_hash: aba3d6ed5ada86e6cf3d6955177f7ec0ea04befc
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/pw-cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-cat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-cat

PipeWire를 통해 오디오 파일을 재생하고 녹음.
더 많은 정보: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- 기본 대상으로 WAV 파일 재생:

`pw-cat --playback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>

- 지정된 리샘플러 품질(기본값 4)로 WAV 파일 재생:

`pw-cat --quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..15</span>` --playback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>

- 125% 볼륨 수준으로 샘플 녹음:

`pw-cat --record --volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.25</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>

- 다른 샘플 레이트를 사용하여 샘플 녹음:

`pw-cat --record --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>
