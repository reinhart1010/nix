---
layout: page
title: common/uudecode (한국어)
description: "`uuencode`로 인코딩된 파일을 디코딩."
content_hash: ed54d89f0f9c43536bbe37c0e2b35842a6564d91
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/uudecode.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/uudecode.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uudecode

`uuencode`로 인코딩된 파일을 디코딩.
더 많은 정보: <https://manned.org/uudecode>.

- `uuencode`로 인코딩된 파일을 디코딩하여 `stdout`에 출력:

`uudecode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인코딩된_파일</span>

- `uuencode`로 인코딩된 파일을 디코딩하여 파일에 저장:

`uudecode -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디코딩된_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인코딩된_파일</span>
