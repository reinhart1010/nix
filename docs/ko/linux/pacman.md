---
layout: page
title: linux/pacman (한국어)
description: "Arch Linux 패키지 관리 도구."
content_hash: 1684ceb765b5181b33996d8818d57aaa3be3d29b
last_modified_at: 2024-06-10
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman

Arch Linux 패키지 관리 도구.
같이 보기: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
더 많은 정보: <https://man.archlinux.org/man/pacman.8>.

- 모든 패키지를 동기화하고 업데이트:

`sudo pacman -Syu`

- 새 패키지 설치:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 패키지 및 의존성 제거:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 파일이 포함된 패키지를 데이터베이스에서 검색:

`pacman -F "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>`"`

- 설치된 패키지 및 버전 나열:

`pacman -Q`

- 명시적으로 설치된 패키지 및 버전만 나열:

`pacman -Qe`

- 고아 패키지(의존성으로 설치되었지만 더 이상 어떤 패키지도 필요로 하지 않는 패키지) 나열:

`pacman -Qtdq`

- 전체 `pacman` 캐시 삭제:

`sudo pacman -Scc`
