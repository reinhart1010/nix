---
layout: page
title: common/bc (한국어)
description: "계산기의 기능을 수행합니다."
content_hash: 4e3537c1df00346ca03d064f1dd14c7b8913d08a
last_modified_at: 2023-11-12
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
  - title: 中文 version
    url: /zh/common/bc.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bc

계산기의 기능을 수행합니다.
더 많은 정보: <https://manned.org/man/bc.1>.

- 표준 Math 라이브러리를 사용한 대화형 모드에서 계산기 실행하기:

`bc -l`

- 계산 결과 표현법:

`bc <<< "(1 + 2) * 2 ^ 2"`

- 계산 및 표현되는 소수 자릿수를 10으로 지정하기:

`bc <<< "scale=10; 5 / 3"`

- mathlib를 사용하여 sin 및 cosine의 계산식 표현하기:

`bc -l <<< "s(1) + c(1)"`
