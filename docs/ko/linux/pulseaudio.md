---
layout: page
title: linux/pulseaudio (한국어)
description: "PulseAudio 사운드 시스템 데몬 및 관리자."
content_hash: 26df9b1fec2801973692f558f6eab011fba8d7a9
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pulseaudio.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/pulseaudio.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pulseaudio.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pulseaudio.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pulseaudio

PulseAudio 사운드 시스템 데몬 및 관리자.
더 많은 정보: <https://www.freedesktop.org/wiki/Software/PulseAudio/>.

- PulseAudio가 실행 중인지 확인 (0이 아닌 종료 코드는 실행 중이 아님을 의미):

`pulseaudio --check`

- 백그라운드에서 PulseAudio 데몬 시작:

`pulseaudio --start`

- 실행 중인 PulseAudio 데몬 종료:

`pulseaudio --kill`

- 사용 가능한 모듈 나열:

`pulseaudio --dump-modules`

- 현재 실행 중인 데몬에 모듈과 지정된 인수를 로드:

`pulseaudio --load="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수</span>`"`
