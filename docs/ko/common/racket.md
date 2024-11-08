---
layout: page
title: common/racket (한국어)
description: "Racket 언어 인터프리터."
content_hash: c7308ebfd1125bf5548765f9f78c92c23151854f
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/racket.html
    icon: bi bi-globe
tldri18n_status: 2
---
# racket

Racket 언어 인터프리터.
더 많은 정보: <https://racket-lang.org>.

- REPL(대화형 셸) 시작:

`racket`

- Racket 스크립트 실행:

`racket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.rkt</span>

- Racket 표현식 실행:

`racket --eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식</span>`"`

- 모듈을 스크립트로 실행 (옵션 목록 종료):

`racket --lib `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>` --main `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수</span>

- `typed/racket` 해시랭을 위한 REPL(대화형 셸) 시작:

`racket -I typed/racket`
