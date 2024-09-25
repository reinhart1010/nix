---
layout: page
title: linux/pacman-sync (한국어)
description: "Arch Linux 패키지 관리 도구."
content_hash: f549194d15efaa06ae17ac44c89a10568b6e7c2d
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-sync.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-sync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-sync.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-sync.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-sync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --sync

Arch Linux 패키지 관리 도구.
같이 보기: `pacman`.
더 많은 정보: <https://manned.org/pacman.8>.

- 새 패키지 설치:

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 모든 패키지 동기화 및 업데이트 (`--downloadonly`를 추가하여 패키지를 다운로드만 하고 업데이트하지 않음):

`sudo pacman --sync --refresh --sysupgrade`

- 모든 패키지를 업데이트하고 새 패키지를 확인 없이 설치:

`sudo pacman --sync --refresh --sysupgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 정규 표현식 또는 키워드로 패키지 데이터베이스 검색:

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>`"`

- 패키지 정보 표시:

`pacman --sync --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 업데이트 중 충돌하는 파일 덮어쓰기:

`sudo pacman --sync --refresh --sysupgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 모든 패키지를 동기화 및 업데이트하지만 특정 패키지는 무시 (여러 번 사용 가능):

`sudo pacman --sync --refresh --sysupgrade --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치되지 않은 패키지와 사용되지 않는 저장소를 캐시에서 제거 (모든 패키지를 정리하려면 `--clean` 플래그를 두 번 사용):

`sudo pacman --sync --clean`
