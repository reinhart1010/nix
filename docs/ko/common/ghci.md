---
layout: page
title: common/ghci (한국어)
description: "Glasgow Haskell 컴파일러 대화형 환경."
content_hash: 0c5bc83d0124e32dc52aa502bf49b1f4714f2ae3
last_modified_at: 2024-10-22
related_topics:
  - title: English version
    url: /en/common/ghci.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ghci.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ghci

Glasgow Haskell 컴파일러 대화형 환경.
더 많은 정보: <https://downloads.haskell.org/ghc/latest/docs/html/users_guide/ghci.html>.

- REPL (대화형 쉘)을 시작:

`ghci`

- REPL을 시작하고 지정된 Haskell 소스 파일을 로드:

`ghci `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_파일.hs</span>

- REPL을 시작하고 언어 옵션을 활성화:

`ghci -X`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어_옵션</span>

- REPL을 시작하고 일젓 수준의 컴파일러 경고(예: `all` 또는 `compact`)를 활성화:

`ghci -W`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경고_수준</span>

- 소스 파일을 찾기 위해 콜론으로 구분된 디렉터리 목록으로 REPL을 시작:

`ghci -i`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1:경로/대상/디렉터리2:...</span>
