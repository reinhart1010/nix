---
layout: page
title: osx/notifyd (한국어)
description: "알림 서버."
content_hash: 3ba389766ef5c2395e2c9c19cdf357111ebf4520
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/notifyd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# notifyd

알림 서버.
수동으로 호출하지 않아야 합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/notifyd.8.html>.

- 데몬 시작:

`notifyd`

- 디버그 메시지를 기본 로그 [f]파일(`/var/log/notifyd.log`)로 기록:

`notifyd -d`

- 디버그 메시지를 대체 로그 [f]파일로 기록:

`notifyd -d -log_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로그_파일</span>
