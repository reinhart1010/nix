---
layout: page
title: linux/pacman-deptest (한국어)
description: "지정된 각 의존성을 확인하고 시스템에 현재 충족되지 않은 의존성 목록을 반환합니다."
content_hash: 384c2e3363b91529d20bd02604299875dc118815
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-deptest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --deptest

지정된 각 의존성을 확인하고 시스템에 현재 충족되지 않은 의존성 목록을 반환합니다.
같이 보기: `pacman`.
더 많은 정보: <https://manned.org/pacman.8>.

- 설치되지 않은 의존성의 패키지 이름을 출력:

`pacman --deptest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 설치된 패키지가 주어진 최소 버전을 충족하는지 확인:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>=5</span>`"`

- 패키지의 최신 버전이 설치되었는지 확인:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>5</span>`"`

- 도움말 표시:

`pacman --deptest --help`
