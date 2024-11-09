---
layout: page
title: linux/arithmetic (한국어)
description: "간단한 산술 문제 퀴즈."
content_hash: 0d93b92f3a40ec68b685ae979f5acb2475efd71e
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/linux/arithmetic.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/arithmetic.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arithmetic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arithmetic

간단한 산술 문제 퀴즈.
더 많은 정보: <https://manned.org/arithmetic.6>.

- 산술 퀴즈 시작:

`arithmetic`

- 하나 이상의 산술 [o]연산 기호를 지정하여 해당 문제 받기:

`arithmetic -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-|x|/</span>

- 범위 지정. 덧셈 및 곱셈 문제는 0부터 범위 내의 숫자가 포함됩니다. 뺄셈 및 나눗셈 문제는 0부터 범위 내의 요구된 결과와 연산할 숫자를 가집니다:

`arithmetic -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>
