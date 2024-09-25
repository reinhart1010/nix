---
layout: page
title: linux/pacman-query (한국어)
description: "Arch Linux 패키지 관리 도구."
content_hash: 2d3eacc93b2a4d3318fed9abab59a0c680993e4a
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-query.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-query.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --query

Arch Linux 패키지 관리 도구.
같이 보기: `pacman`.
더 많은 정보: <https://manned.org/pacman.8>.

- 설치된 패키지와 버전 나열:

`pacman --query`

- 명시적으로 설치된 패키지와 버전만 나열:

`pacman --query --explicit`

- 파일을 소유한 패키지 찾기:

`pacman --query --owns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>

- 설치된 패키지 정보 표시:

`pacman --query --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지가 소유한 파일 나열:

`pacman --query --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 고아 패키지 나열 (의존성으로 설치되었지만 더 이상 어떤 패키지도 필요로 하지 않는 패키지):

`pacman --query --unrequired --deps --quiet`

- 저장소에서 찾을 수 없는 설치된 패키지 나열:

`pacman --query --foreign`

- 오래된 패키지 나열:

`pacman --query --upgrades`
