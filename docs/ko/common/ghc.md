---
layout: page
title: common/ghc (한국어)
description: "Glasgow Haskell 컴파일러."
content_hash: ed4b90fb21374f326fe195e2b33eaf703f5c4828
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/ghc.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ghc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ghc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ghc

Glasgow Haskell 컴파일러.
하스켈 소스 파일을 컴파일하고 링크.
더 많은 정보: <https://www.haskell.org/ghc>.

- 현재 디렉터리에서 모든 모듈을 찾아 컴파일:

`ghc Main`

- 단일 파일 컴파일:

`ghc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.hs</span>

- 추가 최적화를 사용해 컴파일:

`ghc -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.hs</span>

- 객체 파일(.o) 생성 후 컴파일 중지:

`ghc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.hs</span>

- REPL (대화형 쉘)을 시작:

`ghci`

- 단일 표현식 평가:

`ghc -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식</span>
