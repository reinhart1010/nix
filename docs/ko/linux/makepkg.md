---
layout: page
title: linux/makepkg (한국어)
description: "`pacman`과 함께 사용할 수 있는 패키지를 생성합니다."
content_hash: 7fef09065c6015f26786d8d8060fa5895ef13bc5
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/makepkg.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/makepkg.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/makepkg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/makepkg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/makepkg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># makepkg

`pacman`과 함께 사용할 수 있는 패키지를 생성합니다.
기본적으로 현재 작업 디렉토리의 `PKGBUILD` 파일을 사용합니다.
더 많은 정보: <https://manned.org/makepkg.8>.

- 패키지 생성:

`makepkg`

- 패키지를 생성하고 의존성을 설치:

`makepkg --syncdeps`

- 패키지를 생성하고 의존성을 설치한 다음 시스템에 설치:

`makepkg --syncdeps --install`

- 패키지를 생성하되 소스의 해시 검사를 건너뜀:

`makepkg --skipchecksums`

- 빌드가 성공한 후 작업 디렉토리 정리:

`makepkg --clean`

- 소스의 해시 검증:

`makepkg --verifysource`

- 소스 정보를 `.SRCINFO`에 생성하고 저장:

`makepkg --printsrcinfo > .SRCINFO`
