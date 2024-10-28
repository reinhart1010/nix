---
layout: page
title: linux/pdftoppm (한국어)
description: "PDF 문서 페이지를 Portable Pixmap(이미지 형식)으로 변환."
content_hash: 6b24c1e7229a33e6f8440b7d84922b06401e4516
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/linux/pdftoppm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pdftoppm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pdftoppm

PDF 문서 페이지를 Portable Pixmap(이미지 형식)으로 변환.
더 많은 정보: <https://manned.org/pdftoppm>.

- 변환할 페이지 범위 지정 (N-첫 번째 페이지, M-마지막 페이지):

`pdftoppm -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">M</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름_접두사</span>

- PDF의 첫 번째 페이지만 변환:

`pdftoppm -singlefile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름_접두사</span>

- 모노크롬 PBM 파일 생성 (컬러 PPM 파일 대신):

`pdftoppm -mono `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름_접두사</span>

- 그레이스케일 PGM 파일 생성 (컬러 PPM 파일 대신):

`pdftoppm -gray `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름_접두사</span>

- PPM 파일 대신 PNG 파일 생성:

`pdftoppm -png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름_접두사</span>
