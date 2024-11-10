---
layout: page
title: linux/paru (한국어)
description: "AUR 헬퍼 및 pacman 래퍼."
content_hash: 2e78495a5b5ed662310c2ebca103d74591afcee8
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/linux/paru.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/paru.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/paru.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/paru.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/paru.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paru

AUR 헬퍼 및 pacman 래퍼.
더 많은 정보: <https://github.com/Morganamilo/paru>.

- 패키지를 대화식으로 검색하고 설치:

`paru `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름_또는_검색어</span>

- 모든 패키지를 동기화하고 업데이트:

`paru`

- AUR 패키지 업그레이드:

`paru -Sua`

- 패키지 정보 확인:

`paru -Si `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- `PKGBUILD` 및 기타 패키지 소스 파일을 AUR 또는 ABS에서 다운로드:

`paru --getpkgbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지의 `PKGBUILD` 파일 표시:

`paru --getpkgbuild --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
