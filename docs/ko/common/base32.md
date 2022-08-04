---
layout: page
title: common/base32 (한국어)
description: "파일 또는 표준 입력을 Base32와 표준 출력으로 인코딩하거나 디코딩함."
content_hash: 188f6de9f9c77d35655280a79f137c1b95c489cf
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
---
# base32

파일 또는 표준 입력을 Base32와 표준 출력으로 인코딩하거나 디코딩함.
더 많은 정보: <https://www.gnu.org/software/coreutils/base32>.

- 파일 인코딩:

`base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- 파일 디코딩:

`base32 --decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- stdin에서 인코딩:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">somecommand</span>` | base32`

- stdin에서 디코딩:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">somecommand</span>` | base32 --decode`
