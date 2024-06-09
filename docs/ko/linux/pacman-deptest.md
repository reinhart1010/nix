---
layout: page
title: linux/pacman-deptest (한국어)
description: "지정된 각 의존성을 확인하고 시스템에 현재 충족되지 않은 의존성 목록을 반환합니다."
content_hash: b1c9517fcf78274916e2d5215b1c47d1ab3d0980
last_modified_at: 2024-06-09
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pacman-deptest.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pacman --deptest

지정된 각 의존성을 확인하고 시스템에 현재 충족되지 않은 의존성 목록을 반환합니다.
같이 보기: `pacman`.
더 많은 정보: <https://man.archlinux.org/man/pacman.8>.

- 설치되지 않은 의존성의 패키지 이름을 출력:

`pacman --deptest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 설치된 패키지가 주어진 최소 버전을 충족하는지 확인:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>=5</span>`"`

- 패키지의 최신 버전이 설치되었는지 확인:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>5</span>`"`

- 도움말 표시:

`pacman --deptest --help`
