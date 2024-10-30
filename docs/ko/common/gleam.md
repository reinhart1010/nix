---
layout: page
title: common/gleam (한국어)
description: "\"확장 가능한 타입 안전 시스템을 구축하기 위한 친숙한 언어!\"인 Gleam용 컴파일러, 빌드 도구, 패키지 관리자 및 코드 포맷터."
content_hash: 1b7ffc2e618881a677912c17180f23b9351a7488
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/gleam.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/gleam.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gleam.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gleam

"확장 가능한 타입 안전 시스템을 구축하기 위한 친숙한 언어!"인 Gleam용 컴파일러, 빌드 도구, 패키지 관리자 및 코드 포맷터.
더 많은 정보: <https://gleam.run/writing-gleam/command-line-reference/>.

- 새로운 gleam 프로젝트 생성:

`gleam new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- gleam 프로젝트 빌드 및 실행:

`gleam run`

- 프로젝트 빌드:

`gleam build`

- 특정 플랫폼 및 런타임에 대한 프로젝트를 실행:

`gleam run --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플랫폼</span>` --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">런타임</span>

- 프로젝트에 16진수 종속성을 추가:

`gleam add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성_이름</span>

- 프로젝트 테스트 실행:

`gleam test`

- 소스 코드 형식 포맷팅:

`gleam format`

- 프로젝트를 확인:

`gleam check`
