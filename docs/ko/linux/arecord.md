---
layout: page
title: linux/arecord (한국어)
description: "ALSA 사운드카드 드라이버용 사운드 레코더."
content_hash: a339d6372551a8fd441a4624a1c59d66992e1e14
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/linux/arecord.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/arecord.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arecord.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/arecord.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># arecord

ALSA 사운드카드 드라이버용 사운드 레코더.
더 많은 정보: <https://manned.org/arecord>.

- "CD" 품질로 녹음 (완료 시 Ctrl-C로 종료):

`arecord -vv --format=cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>

- "CD" 품질로 10초 동안 고정된 길이로 녹음:

`arecord -vv --format=cd --duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>

- 녹음하여 MP3로 저장 (완료 시 Ctrl-C로 종료):

`arecord -vv --format=cd --file-type raw | lame -r - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mp3</span>

- 모든 사운드 카드와 디지털 오디오 장치 나열:

`arecord --list-devices`

- 인터랙티브 인터페이스 허용 (예: 스페이스바나 엔터로 재생 또는 일시 정지):

`arecord --interactive`

- 마이크 테스트를 위해 5초 샘플을 녹음하고 재생:

`arecord -d 5 test-mic.wav && aplay test-mic.wav && rm test-mic.wav`
