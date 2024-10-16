---
layout: page
title: common/elm (한국어)
description: "Elm 소스 파일을 컴파일하고 실행."
content_hash: ddc67a60e03ca1b6bf848f9ac4d38c265b54df9b
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/elm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/elm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/elm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># elm

Elm 소스 파일을 컴파일하고 실행.
더 많은 정보: <https://elm-lang.org>.

- Elm 프로젝트를 초기화하고, elm.json 파일을 생성:

`elm init`

- 대화형 Elm 쉘을 시작:

`elm repl`

- Elm 파일을 컴파일하고, 결과를 `index.html` 파일로 출력:

`elm make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스</span>

- Elm 파일을 컴파일하고, 결과를 JavaScript 파일로 출력:

`elm make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>`.js`

- 페이지 로드 시 Elm 파일을 컴파일하는 로컬 웹 서버 시작:

`elm reactor`

- <https://package.elm-lang.org>에서 Elm 패키지를 설치:

`elm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
