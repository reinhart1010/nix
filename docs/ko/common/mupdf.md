---
layout: page
title: common/mupdf (한국어)
description: "경량 PDF, XPS 및 전자책 뷰어."
content_hash: f9104aecd8d30631f188f019673b6655566dd692
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/mupdf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mupdf

경량 PDF, XPS 및 전자책 뷰어.
더 많은 정보: <https://www.mupdf.com>.

- 첫 페이지에서 PDF 열기:

`mupdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 3페이지에서 PDF 열기:

`mupdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- 비밀번호로 보호된 PDF 열기:

`mupdf -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 초기 확대 수준(72 DPI)으로 PDF 열기:

`mupdf -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">72</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 색상이 반전된 PDF 열기:

`mupdf -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 빨간색 #FF0000 틴트가 적용된 PDF 열기 (16진수 색상 구문 RRGGBB):

`mupdf -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FF0000</span>

- 안티앨리어싱 없이 PDF 열기 (0 = 끔, 8 = 최고):

`mupdf -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
