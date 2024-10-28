---
layout: page
title: common/pdfunite (한국어)
description: "PDF 병합 도구."
content_hash: 4b41fbecd2e394432ec6bd52edf700a92fa4fe32
last_modified_at: 2024-10-28
related_topics:
  - title: Deutsch version
    url: /de/common/pdfunite.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pdfunite.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pdfunite.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pdfunite

PDF 병합 도구.
더 많은 정보: <https://github.com/mtgrosser/pdfunite>.

- 2개의 PDF를 하나의 PDF로 병합:

`pdfunite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일A.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일B.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/병합된_출력.pdf</span>

- 폴더 내의 PDF 파일을 하나의 PDF로 병합:

`pdfunite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더/*.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/병합된_출력.pdf</span>
