---
layout: page
title: linux/apt-get (한국어)
description: "Debian 및 Ubuntu 패키지 관리 도구."
content_hash: ba06b4d6bd0f6e85cc57bf346010a79e65e9bbc0
last_modified_at: 2024-11-08
related_topics:
  - title: العربية version
    url: /ar/linux/apt-get.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt-get.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt-get.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apt-get.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apt-get

Debian 및 Ubuntu 패키지 관리 도구.
`apt-cache`를 사용하여 패키지를 검색하세요.
Ubuntu 16.04 이후 버전에서는 대화형 사용 시 `apt` 사용을 권장합니다.
더 많은 정보: <https://manned.org/apt-get.8>.

- 사용 가능한 패키지 및 버전 목록 업데이트 (다른 `apt-get` 명령어 실행 전에 권장됨):

`apt-get update`

- 패키지 설치 또는 최신 버전으로 업데이트:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 및 구성 파일 제거:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 모든 패키지를 최신 버전으로 업그레이드:

`apt-get upgrade`

- 로컬 저장소 정리 - 중단된 다운로드로 인해 더 이상 다운로드할 수 없는 패키지 파일(`.deb`) 제거:

`apt-get autoclean`

- 더 이상 필요하지 않은 모든 패키지 제거:

`apt-get autoremove`

- 설치된 패키지 업그레이드 (`upgrade`와 유사하지만, 불필요한 패키지를 제거하고 새로운 의존성을 충족하기 위해 추가 패키지를 설치):

`apt-get dist-upgrade`
