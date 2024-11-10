---
layout: page
title: linux/xbps-query (한국어)
description: "패키지 및 저장소 정보를 조회하는 XBPS 유틸리티."
content_hash: ea7c074658d55af2ee7c4865d25677c3126a35dc
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/xbps-query.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/xbps-query.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xbps-query.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xbps-query

패키지 및 저장소 정보를 조회하는 XBPS 유틸리티.
같이 보기: `xbps`.
더 많은 정보: <https://manned.org/xbps-query.1>.

- 정규 표현식 또는 키워드를 사용하여 원격 저장소에서 패키지 검색 (`--regex`가 생략된 경우 키워드 사용):

`xbps-query --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식|키워드</span>` --repository --regex`

- 설치된 패키지에 대한 정보 표시:

`xbps-query --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 원격 저장소의 패키지 정보 표시:

`xbps-query --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --repository`

- 패키지 데이터베이스에 등록된 패키지 나열:

`xbps-query --list-pkgs`

- 명시적으로 설치된 패키지 나열 (의존성으로 자동 설치되지 않은 패키지):

`xbps-query --list-manual-pkgs`
