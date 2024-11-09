---
layout: page
title: linux/dnf5 (한국어)
description: "RHEL, Fedora, CentOS를 위한 패키지 관리 도구(dnf를 대체하며, dnf는 yum을 대체)."
content_hash: 533286d65370226941d77ca9ad6683d40b570319
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dnf5.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf5.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dnf5.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnf5

RHEL, Fedora, CentOS를 위한 패키지 관리 도구(dnf를 대체하며, dnf는 yum을 대체).
DNF5는 C++로 다시 작성된 DNF 패키지 관리자로, 성능이 향상되고 크기가 작아졌습니다.
다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
더 많은 정보: <https://dnf5.readthedocs.io>.

- 설치된 패키지를 최신 버전으로 업그레이드:

`sudo dnf5 upgrade`

- 키워드로 패키지 검색:

`dnf5 search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드1 키워드2 ...</span>

- 패키지에 대한 세부 정보 표시:

`dnf5 info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 새 패키지 설치 (`-y`를 사용하여 모든 메시지 자동 확인):

`sudo dnf5 install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 패키지 제거:

`sudo dnf5 remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 설치된 패키지 나열:

`dnf5 list --installed`

- 특정 명령을 제공하는 패키지 찾기:

`dnf5 provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 캐시된 데이터 제거 또는 만료:

`sudo dnf5 clean all`
