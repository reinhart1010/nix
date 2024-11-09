---
layout: page
title: common/tldr-lint (한국어)
description: "`tldr` 페이지를 검사하고 포맷."
content_hash: 2689d10f71a5fc26b66fb17f491c4008f6c0399d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tldr-lint.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tldr-lint.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tldr-lint.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tldr-lint.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr-lint.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr-lint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tldr-lint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tldr-lint

`tldr` 페이지를 검사하고 포맷.
더 많은 정보: <https://github.com/tldr-pages/tldr-lint>.

- 모든 페이지 검사:

`tldr-lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_디렉토리</span>

- 특정 페이지를 포맷하여 `stdout`에 출력:

`tldr-lint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지.md</span>

- 모든 페이지를 제자리에서 포맷:

`tldr-lint --format --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_디렉토리</span>
