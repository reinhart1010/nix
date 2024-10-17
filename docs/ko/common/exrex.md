---
layout: page
title: common/exrex (한국어)
description: "정규식에 대해 모두/무작위로 일치하는 문자열을 생성."
content_hash: 46af855a82393e1de79ea74c988b7874402ed606
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/exrex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exrex

정규식에 대해 모두/무작위로 일치하는 문자열을 생성.
정규식을 단순화할 수 있음.
더 많은 정보: <https://github.com/asciimoo/exrex>.

- 정규식과 일치하는 가능한 모든 문자열을 생성:

`exrex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`'`

- 정규식과 일치하는 임의의 문자열을 생성:

`exrex --random '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`'`

- 정규식과 일치하는 최대 100개의 문자열을 생성:

`exrex --max-number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`'`

- 사용자 정의 구분 기호 문자열로 결합된, 정규식과 일치하는 가능한 모든 문자열을 생성:

`exrex --delimiter "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">, </span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`'`

- 정규식과 일치하는 가능한 모든 문자열의 개수를 출력:

`exrex --count '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`'`

- 정규 표현식을 단순화:

`exrex --simplify '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ab|ac</span>`'`

- 눈 출력:

`exrex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[oO0](_)[oO0]</span>`'`

- 보트 출력:

`exrex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">( {20}(\| *\\|-{22}|\|)|\.={50}| ( ){0,5}\\\.| {12}~{39})</span>`'`
