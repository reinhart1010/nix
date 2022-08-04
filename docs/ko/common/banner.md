---
layout: page
title: common/banner (한국어)
description: "주어진 인자를 큰 ASCII art로 출력."
content_hash: 1300046eff4a07745e107f2e800a4b540c1ac5d0
related_topics:
  - title: English version
    url: /en/common/banner.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/banner.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/banner.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/banner.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/banner.html
    icon: bi bi-globe
---
# banner

주어진 인자를 큰 ASCII art로 출력.
더 많은 정보: <https://manned.org/banner>.

- 텍스트 메시지를 큰 배너로 출력(따옴표는 선택 사항):

`banner "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- 텍스트 메시지를 너비가 50자인 배너로 출력:

`banner -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- stdin에서 텍스트 읽기:

`banner`
