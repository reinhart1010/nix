---
layout: page
title: linux/zypper (한국어)
description: "SUSE 및 openSUSE 패키지 관리 도구."
content_hash: 2659d23bf7d90d822755fe65cc5659654366fce9
last_modified_at: 2024-10-29
related_topics:
  - title: català version
    url: /ca/linux/zypper.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/zypper.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/zypper.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/zypper.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/zypper.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/zypper.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/zypper.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/zypper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zypper

SUSE 및 openSUSE 패키지 관리 도구.
다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
더 많은 정보: <https://en.opensuse.org/SDB:Zypper_manual>.

- 사용 가능한 패키지 및 버전 목록 동기화:

`zypper refresh`

- 새 패키지 설치:

`zypper install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거:

`zypper remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 패키지를 최신 버전으로 업그레이드:

`zypper update`

- 키워드를 통한 패키지 검색:

`zypper search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 구성된 저장소에 대한 정보 표시:

`zypper repos --sort-by-priority`
