---
layout: page
title: common/scheme (한국어)
description: "MIT Scheme 언어 인터프리터 및 REPL(대화형 셸)."
content_hash: afdaa7c9c7ffa0f691b9466d0df69230f60d995f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/scheme.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scheme

MIT Scheme 언어 인터프리터 및 REPL(대화형 셸).
더 많은 정보: <https://www.gnu.org/software/mit-scheme>.

- REPL(대화형 셸) 시작:

`scheme`

- Scheme 프로그램 실행(REPL 출력 없음):

`scheme --quiet < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.scm</span>

- Scheme 프로그램을 REPL에 로드:

`scheme --load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.scm</span>

- Scheme 표현식을 REPL에 로드:

`scheme --eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(define foo 'x)</span>`"`

- 조용한 모드로 REPL 열기:

`scheme --quiet`
