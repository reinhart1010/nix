---
layout: page
title: linux/pacman-files (한국어)
description: "Arch Linux 패키지 관리 도구."
content_hash: 19d2ff57ffcc58e6a4a0c1e08766152caaec0ea3
last_modified_at: 2024-06-10
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-files.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-files.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-files.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-files.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-files.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --files

Arch Linux 패키지 관리 도구.
같이 보기: `pacman`, `pkgfile`.
더 많은 정보: <https://man.archlinux.org/man/pacman.8>.

- 패키지 데이터베이스 업데이트:

`sudo pacman --files --refresh`

- 특정 파일을 소유한 패키지 찾기:

`pacman --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>

- 정규 표현식을 사용하여 특정 파일을 소유한 패키지 찾기:

`pacman --files --regex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규표현식</span>`'`

- 패키지 이름만 나열:

`pacman --files --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>

- 특정 패키지가 소유한 파일 나열:

`pacman --files --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 도움말 표시:

`pacman --files --help`
