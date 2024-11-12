---
layout: page
title: osx/sntp (한국어)
description: "매우 간단한 네트워크 시간 프로토콜 클라이언트 프로그램."
content_hash: 316cbcd87887ee0ca03a6a31eaba30c3a58ac723
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/sntp.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/sntp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sntp

매우 간단한 네트워크 시간 프로토콜 클라이언트 프로그램.
더 많은 정보: <https://keith.github.io/xcode-man-pages/sntp.1>.

- 지정된 SNTP 서버에 쿼리하고 시간을 표시:

`sntp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool.ntp.org</span>

- 지정된 SNTP 서버로 시스템 시계를 동기화:

`sudo sntp -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool.ntp.org</span>

- 디버그 로깅 활성화:

`sntp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool.ntp.org</span>
