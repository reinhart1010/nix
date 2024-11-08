---
layout: page
title: linux/aptitude (한국어)
description: "Debian 및 Ubuntu 패키지 관리 도구."
content_hash: 6c4832db1107a42041ec2df9ff16bf0005d4e7ef
last_modified_at: 2024-11-08
related_topics:
  - title: català version
    url: /ca/linux/aptitude.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/aptitude.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aptitude.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aptitude.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aptitude.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aptitude.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/aptitude.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/aptitude.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/aptitude.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/aptitude.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aptitude

Debian 및 Ubuntu 패키지 관리 도구.
더 많은 정보: <https://manned.org/aptitude.8>.

- 사용 가능한 패키지 및 버전 목록 동기화. 이 명령은 다른 `aptitude` 명령을 실행하기 전에 먼저 실행해야 합니다:

`aptitude update`

- 새 패키지 및 그 의존성 설치:

`aptitude install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 검색:

`aptitude search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 패키지 검색 (`?installed`는 `aptitude` 검색 용어입니다):

`aptitude search '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`)'`

- 특정 패키지 및 해당 패키지에 의존하는 모든 패키지 제거:

`aptitude remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 패키지를 가장 최신 버전으로 업그레이드:

`aptitude upgrade`

- 설치된 패키지 업그레이드 (`aptitude upgrade`와 유사)하며, 불필요한 패키지를 제거하고 새로운 패키지 의존성을 충족하기 위해 추가 패키지 설치:

`aptitude full-upgrade`

- 자동 업그레이드되지 않도록 설치된 패키지를 보류:

`aptitude hold '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`)'`
