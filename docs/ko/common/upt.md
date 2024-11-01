---
layout: page
title: common/upt (한국어)
description: "다양한 운영 체제에서 패키지를 관리하기 위한 통합 인터페이스로, Windows, 여러 Linux 배포판, macOS, FreeBSD, Haiku 등을 지원합니다."
content_hash: c7d642fae40fd4b331eaf4addb24e9acbb060724
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/upt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/upt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/upt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># upt

다양한 운영 체제에서 패키지를 관리하기 위한 통합 인터페이스로, Windows, 여러 Linux 배포판, macOS, FreeBSD, Haiku 등을 지원합니다.
기본 OS 패키지 관리자가 설치되어 있어야 합니다.
같이 보기: `flatpak`, `brew`, `scoop`, `apt`, `dnf`.
더 많은 정보: <https://github.com/sigoden/upt>.

- 사용 가능한 패키지 목록 업데이트:

`upt update`

- 특정 패키지 검색:

`upt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_어구</span>

- 패키지에 대한 정보 표시:

`upt info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 패키지 설치:

`upt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 패키지 제거:

`upt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remove|uninstall</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 모든 패키지 업그레이드:

`upt upgrade`

- 특정 패키지 업그레이드:

`upt upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 패키지 목록 나열:

`upt list`
