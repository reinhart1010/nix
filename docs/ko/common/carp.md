---
layout: page
title: common/carp (한국어)
description: "Carp용 REPL 및 빌드 도구."
content_hash: 1b1b1a7976fb7f6a0c5108ad98ae1d68f6ca09b0
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/carp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# carp

Carp용 REPL 및 빌드 도구.
더 많은 정보: <https://carp-lang.github.io/carp-docs/Manual.html>.

- REPL (대화형 셸)을 시작:

`carp`

- 사용자 정의 프롬프트로 REPL을 시작:

`carp --prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">> </span>`"`

- `carp` 파일을 빌드:

`carp -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.carp</span>

- 파일 빌드 및 실행:

`carp -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.carp</span>

- 최적화가 활성화된 파일을 빌드:

`carp -b --optimize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.carp</span>

- 파일을 C 코드로 변환:

`carp --generate-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.carp</span>
