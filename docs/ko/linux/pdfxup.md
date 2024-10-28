---
layout: page
title: linux/pdfxup (한국어)
description: "PDF 페이지를 N-up으로 배치."
content_hash: b45f036f3ba0848964ec1242c1c1ad01acaec7c3
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/linux/pdfxup.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pdfxup.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pdfxup

PDF 페이지를 N-up으로 배치.
N-up은 여러 페이지를 하나의 페이지에 축소 및 회전하여 그리드 형태로 배치하는 것을 의미합니다.
더 많은 정보: <https://ctan.org/pkg/pdfxup>.

- 2-up PDF 생성:

`pdfxup -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>

- 페이지당 3열 및 2행으로 PDF 생성:

`pdfxup -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>

- 소책자 모드(2-up, 페이지가 접혔을 때 책 형태로 정렬)로 PDF 생성:

`pdfxup -b -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>
