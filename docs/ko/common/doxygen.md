---
layout: page
title: common/doxygen (한국어)
description: "다양한 프로그래밍 언어의 문서화 시스템."
content_hash: cfe5b2fba64ca9064a41dc993903ac267d5797ef
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/doxygen.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/doxygen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/doxygen.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doxygen.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doxygen

다양한 프로그래밍 언어의 문서화 시스템.
더 많은 정보: <https://www.doxygen.nl>.

- 기본 템플릿 구성 파일 `Doxyfile`을 생성:

`doxygen -g`

- 템플릿 구성 파일 생성:

`doxygen -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일</span>

- 기존 구성 파일을 사용하여 문서 생성:

`doxygen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일</span>
