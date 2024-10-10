---
layout: page
title: windows/w32tm (한국어)
description: "w32time 시간 동기화 서비스를 쿼리하고 제어합니다."
content_hash: f1191ebee9eb22490bf334c5ab2e6686a8e873c6
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/windows/w32tm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/w32tm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># w32tm

w32time 시간 동기화 서비스를 쿼리하고 제어합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings>.

- 시간 동기화의 현재 상태 표시:

`w32tm /query /status /verbose`

- 시간 서버에 대한 시간 오프셋 그래프 표시:

`w32tm /stripchart /computer:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간_서버</span>

- 시간 서버에서 NTP 응답 표시:

`w32tm /stripchart /packetinfo /samples:1 /computer:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간_서버</span>

- 현재 사용되는 시간 서버의 상태 표시:

`w32tm /query /peers`

- w32time 서비스의 구성 표시 (관리자 권한으로 실행):

`w32tm /query /configuration`

- 강제 시간 재동기화를 즉시 실행 (관리자 권한으로 실행):

`w32tm /resync /force`

- w32time 디버그 로그를 파일에 쓰기 (관리자 권한으로 실행):

`w32tm /debug /enable /file:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\debug.log</span>` /size:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10000000</span>` /entries:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0-300</span>
