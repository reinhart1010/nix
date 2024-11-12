---
layout: page
title: osx/port (한국어)
description: "macOS 패키지 관리자."
content_hash: 29cec5601c6ed5418fa1d2d589ced4a8687f4bca
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/port.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/port.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/port.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/port.html
    icon: bi bi-globe
tldri18n_status: 2
---
# port

macOS 패키지 관리자.
더 많은 정보: <https://www.macports.org>.

- 패키지 검색:

`port search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_어</span>

- 패키지 설치:

`sudo port install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 패키지 나열:

`port installed`

- 포트를 업데이트하고 사용 가능한 패키지의 최신 목록 가져오기:

`sudo port selfupdate`

- 오래된 패키지 업그레이드:

`sudo port upgrade outdated`

- 설치된 패키지의 이전 버전 제거:

`sudo port uninstall inactive`
