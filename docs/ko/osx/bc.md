---
layout: page
title: osx/bc (한국어)
description: "임의 정밀도 계산기 언어."
content_hash: d06f013ae2ab02b61052049e6733c1ee963d40b7
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/bc.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/bc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/bc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/bc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bc

임의 정밀도 계산기 언어.
같이 보기: `dc`.
더 많은 정보: <https://keith.github.io/xcode-man-pages/bc.1.html>.

- 대화형 세션 시작:

`bc`

- 표준 수학 라이브러리를 활성화하여 대화형 세션 시작:

`bc --mathlib`

- 수식 계산:

`bc --expression='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'`

- 스크립트 실행:

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.bc</span>

- 지정된 스케일로 수식 계산:

`bc --expression='scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'`

- `mathlib`을 사용하여 사인/코사인/아크탄젠트/자연 로그/지수 함수 계산:

`bc --mathlib --expression='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)'`
