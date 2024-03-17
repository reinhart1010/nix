---
layout: page
title: common/base32 (한국어)
description: "파일 또는 표준 입력을 Base32와 표준 출력으로 인코딩하거나 디코딩함."
content_hash: c60e9f473ccdef67e2fb621a27fb344ece5f0a6a
last_modified_at: 2024-03-17
related_topics:
  - title: English version
    url: /en/common/base32.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/base32.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/base32.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/base32.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/base32.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/base32.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/base32.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/base32.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># base32

파일 또는 표준 입력을 Base32와 표준 출력으로 인코딩하거나 디코딩함.
더 많은 정보: <https://www.gnu.org/software/coreutils/base32>.

- 파일 인코딩:

`base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- 파일 디코딩:

`base32 --decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- `stdin`에서 인코딩:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">somecommand</span>` | base32`

- `stdin`에서 디코딩:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">somecommand</span>` | base32 --decode`
