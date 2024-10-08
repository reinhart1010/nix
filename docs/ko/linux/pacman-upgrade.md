---
layout: page
title: linux/pacman-upgrade (한국어)
description: "Arch Linux 패키지 관리 도구."
content_hash: 06e65f3ac175e02870d2874d9915fc53455e9221
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --upgrade

Arch Linux 패키지 관리 도구.
같이 보기: `pacman`.
더 많은 정보: <https://manned.org/pacman.8>.

- 파일에서 하나 이상의 패키지 설치:

`sudo pacman --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지1.pkg.tar.zst</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지2.pkg.tar.zst</span>

- 확인 없이 패키지 설치:

`sudo pacman --upgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.pkg.tar.zst</span>

- 패키지 설치 중 충돌하는 파일 덮어쓰기:

`sudo pacman --upgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.pkg.tar.zst</span>

- 의존성 버전 검사를 건너뛰고 패키지 설치:

`sudo pacman --upgrade --nodeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.pkg.tar.zst</span>

- 영향을 받을 패키지 목록 표시 (패키지를 설치하지 않음):

`pacman --upgrade --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.pkg.tar.zst</span>

- 도움말 표시:

`pacman --upgrade --help`
