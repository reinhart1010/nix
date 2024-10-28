---
layout: page
title: common/pdfimages (한국어)
description: "PDF에서 이미지를 추출하는 유틸리티."
content_hash: 35edb288e39d2d91195f488e26c65b439de0ee8d
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/common/pdfimages.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/pdfimages.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pdfimages.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pdfimages

PDF에서 이미지를 추출하는 유틸리티.
더 많은 정보: <https://manned.org/pdfimages>.

- PDF 파일에서 모든 이미지를 추출하여 PNG로 저장:

`pdfimages -png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름_접두사</span>

- 3페이지부터 5페이지까지의 이미지 추출:

`pdfimages -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름_접두사</span>

- PDF 파일에서 이미지를 추출하고 출력 파일 이름에 페이지 번호 포함:

`pdfimages -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름_접두사</span>

- PDF 파일의 모든 이미지에 대한 정보 나열:

`pdfimages -list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>
