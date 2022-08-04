---
layout: page
title: common/bc (한국어)
description: "계산기의 기능을 수행합니다."
content_hash: 4e3537c1df00346ca03d064f1dd14c7b8913d08a
related_topics:
  - title: English version
    url: /en/common/bc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bc.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
