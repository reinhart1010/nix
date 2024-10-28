---
layout: page
title: common/pdfgrep (한국어)
description: "PDF 파일에서 텍스트 검색."
content_hash: d1dc04385fe5e33d09fc02720b33a56b61de3ce8
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/common/pdfgrep.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pdfgrep.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pdfgrep.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pdfgrep

PDF 파일에서 텍스트 검색.
더 많은 정보: <https://pdfgrep.org>.

- PDF에서 패턴과 일치하는 줄 찾기:

`pdfgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.pdf</span>

- 각 일치하는 줄에 대해 파일 이름과 페이지 번호 포함:

`pdfgrep --with-filename --page-number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.pdf</span>

- "foo"로 시작하는 줄을 대소문자 구분 없이 검색하고 처음 3개의 일치 항목 반환:

`pdfgrep --max-count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` --ignore-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'^foo'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.pdf</span>

- 현재 디렉토리에서 `.pdf` 확장자를 가진 파일을 재귀적으로 검색하여 패턴 찾기:

`pdfgrep --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 현재 디렉토리에서 특정 글롭과 일치하는 파일을 재귀적으로 검색하여 패턴 찾기:

`pdfgrep --recursive --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'*book.pdf'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>
