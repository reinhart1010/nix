---
layout: page
title: common/banner (한국어)
description: "주어진 인자를 큰 ASCII art로 출력."
content_hash: c3bc957973a074f2fa7d2aee8b6f57ef353dfb23
last_modified_at: 2024-10-13
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
tldri18n_status: 2
---
# banner

주어진 인자를 큰 ASCII art로 출력.
더 많은 정보: <https://manned.org/banner>.

- 텍스트 메시지를 큰 배너로 출력(따옴표는 선택 사항):

`banner "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- 텍스트 메시지를 너비가 50자인 배너로 출력:

`banner -w 50 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- `stdin`에서 텍스트 읽기:

`banner`
