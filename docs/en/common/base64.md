---
layout: page
title: common/base64 (English)
description: "Encode or decode file or standard input to/from Base64, to standard output."
content_hash: e195d8d1d2f05eb7c29d87c6fc193537317c980f
last_modified_at: 2022-12-04
related_topics:
  - title: Deutsch version
    url: /de/common/base64.html
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
  - title: 한국어 version
    url: /ko/common/base64.html
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
---
# base64

Encode or decode file or standard input to/from Base64, to standard output.
More information: <https://www.gnu.org/software/coreutils/base64>.

- Encode the contents of a file as base64 and write the result to `stdout`:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Decode the base64 contents of a file and write the result to `stdout`:

`base64 --decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Encode from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">somecommand</span>` | base64`

- Decode from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">somecommand</span>` | base64 --decode`
