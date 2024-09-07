---
layout: page
title: common/adb-reverse (한국어)
description: "안드로이드 디버그 브릿지 역방향: 안드로이드 에뮬레이터 인스턴스 또는 연결된 안드로이드 장치에서 소켓 연결을 역방향으로 수행"
content_hash: bf934e6e80cee9357faa34336bb3cf090bfc0c4b
last_modified_at: 2024-09-07
related_topics:
  - title: English version
    url: /en/common/adb-reverse.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-reverse.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-reverse.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-reverse.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-reverse.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-reverse.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-reverse.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-reverse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb reverse

안드로이드 디버그 브릿지 역방향: 안드로이드 에뮬레이터 인스턴스 또는 연결된 안드로이드 장치에서 소켓 연결을 역방향으로 수행
더 많은 정보: <https://developer.android.com/tools/adb>.

- 에뮬레이터 및 장치의 모든 역방향 소켓 연결을 나열:

`adb reverse --list`

- 에뮬레이터 또는 장치의 TCP 포트를 localhost로 전환:

`adb reverse tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_포트</span>` tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_포트</span>

- 에뮬레이터 또는 장치에서 역방향 소켓 연결을 제거:

`adb reverse --remove tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_포트</span>

- 모든 에뮬레이터 또는 장치에서 역방향 소켓 연결을 제거:

`adb reverse --remove-all`
