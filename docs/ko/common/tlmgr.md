---
layout: page
title: common/tlmgr (한국어)
description: "기존 TeX Live 설치의 패키지 및 구성 옵션 관리."
content_hash: 37b10b6c91948f2676c95447baf963c936d9ebfc
last_modified_at: 2024-11-01
related_topics:
  - title: Deutsch version
    url: /de/common/tlmgr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tlmgr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr

기존 TeX Live 설치의 패키지 및 구성 옵션 관리.
`paper`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 패키지 및 그 의존성 설치:

`tlmgr install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 및 그 의존성 제거:

`tlmgr remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지에 대한 정보 표시:

`tlmgr info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 모든 패키지 업데이트:

`tlmgr update --all`

- 업데이트 가능한 항목을 표시하지만 실제로 업데이트하지 않음:

`tlmgr update --list`

- tlmgr의 GUI 버전 시작:

`tlmgr gui`

- 모든 TeX Live 구성 나열:

`tlmgr conf`
