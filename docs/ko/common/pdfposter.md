---
layout: page
title: common/pdfposter (한국어)
description: "큰 시트 PDF를 여러 A4 페이지로 변환하여 인쇄."
content_hash: 7f5719d5791eb32f39c5fa6d1419a0e1bf305431
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/common/pdfposter.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pdfposter.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pdfposter

큰 시트 PDF를 여러 A4 페이지로 변환하여 인쇄.
더 많은 정보: <https://pdfposter.readthedocs.io>.

- A2 포스터를 4개의 A4 페이지로 변환:

`pdfposter --poster-size a2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일.pdf</span>

- A4 포스터를 A3로 확대하고 2개의 A4 페이지 생성:

`pdfposter --scale 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일.pdf</span>
