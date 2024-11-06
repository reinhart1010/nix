---
layout: page
title: common/opusenc (한국어)
description: "WAV 또는 FLAC 오디오를 Opus로 변환."
content_hash: 7774f4daaef7fb386c87fee2236dcfc5559f6f61
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/opusenc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/opusenc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# opusenc

WAV 또는 FLAC 오디오를 Opus로 변환.
더 많은 정보: <https://opus-codec.org/docs/opus-tools/opusenc.html>.

- 기본 옵션을 사용하여 WAV를 Opus로 변환:

`opusenc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.opus</span>

- 스테레오 오디오를 최고 품질 수준으로 변환:

`opusenc --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.opus</span>

- 5.1 서라운드 사운드 오디오를 최고 품질 수준으로 변환:

`opusenc --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1536</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.flac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.opus</span>

- 음성 오디오를 최저 품질 수준으로 변환:

`opusenc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.wav</span>` --downmix-mono --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.opus</span>
