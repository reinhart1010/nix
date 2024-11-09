---
layout: page
title: linux/aur (한국어)
description: "AUR에서 패키지를 빌드하고 로컬 저장소를 관리합니다."
content_hash: fb03e4f29d43b7eb274669fd83632c4aefec1367
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/aur.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aur.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aur

AUR에서 패키지를 빌드하고 로컬 저장소를 관리합니다.
참고: 이 기능을 완전히 사용하려면 `/etc/pacman.conf`에 로컬 저장소가 정의되어 있어야 하며 `vifm`이 설치되어 있어야 합니다.
더 많은 정보: <https://github.com/aurutils/aurutils>.

- AUR 데이터베이스에서 패키지 검색:

`aur search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- AUR에서 패키지와 그 의존성을 다운로드하고 빌드하여 로컬 저장소에 추가:

`aur sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 로컬 저장소에 있는 패키지 [l]목록:

`aur repo --list`

- 로컬 저장소 패키지 [u]업그레이드:

`aur sync --upgrades`

- Vim에서 변경 사항을 보지 않고 패키지를 설치하며, 의존성 설치를 확인하지 않음:

`aur sync --noview --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
