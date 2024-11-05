---
layout: page
title: common/bc (한국어)
description: "임의의 정밀 계산기 언어."
content_hash: 291a66b107081a174296fe905fb8713de30ee9b6
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/bc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bc.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/bc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bc.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bc

임의의 정밀 계산기 언어.
참조: `dc`, `qalc`.
더 많은 정보: <https://manned.org/bc>.

- 대화형 세션을 시작:

`bc`

- 표준 수학 라이브러리([l]ibrary)가 활성화된 상태에서 대화형([i]nteractive) 세션을 시작:

`bc --interactive --mathlib`

- 표현식을 계산:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- 스크립트 실행:

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.bc</span>

- 지정된 척도를 사용해 표현식을 계산:

`echo 'scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- `mathlib`을 사용하여 사인/코사인/아크탄젠트/자연 로그/지수 함수를 계산:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)' | bc --mathlib`

- 인라인 계승 스크립트를 실행:

`echo "define factorial(n) { if (n <= 1) return 1; return n*factorial(n-1); }; factorial(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`)" | bc`
