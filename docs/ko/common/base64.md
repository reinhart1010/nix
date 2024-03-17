---
layout: page
title: common/base64 (한국어)
description: "파일 또는 표준 입력을 Base64와 표준 출력으로 인코딩하거나 디코딩함."
content_hash: d49ae1594354147f77c015b66a97f5b85f7948e2
last_modified_at: 2024-03-17
related_topics:
  - title: Deutsch version
    url: /de/common/base64.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/base64.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/base64.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/base64.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/base64.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/base64.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/base64.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/base64.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/base64.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/base64.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># base64

파일 또는 표준 입력을 Base64와 표준 출력으로 인코딩하거나 디코딩함.
더 많은 정보: <https://www.gnu.org/software/coreutils/base64>.

- 파일 인코딩:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- 파일 디코딩:

`base64 --decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- `stdin`에서 인코딩:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">somecommand</span>` | base64`

- `stdin`에서 디코딩:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">somecommand</span>` | base64 --decode`
