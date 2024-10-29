---
layout: page
title: common/wkhtmltopdf (한국어)
description: "HTML 문서나 웹 페이지를 PDF 파일로 변환하는 오픈 소스 명령줄 도구."
content_hash: 75703e9c2887f746d3e348a6a2826bd1dd3be81e
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/wkhtmltopdf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wkhtmltopdf

HTML 문서나 웹 페이지를 PDF 파일로 변환하는 오픈 소스 명령줄 도구.
더 많은 정보: <https://wkhtmltopdf.org/>.

- HTML 문서를 PDF로 변환:

`wkhtmltopdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.pdf</span>

- PDF 페이지 크기 지정 (`QPrinter`의 `PaperSize`에서 지원되는 크기를 참조):

`wkhtmltopdf --page-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.pdf</span>

- PDF 페이지 여백 설정:

`wkhtmltopdf --margin-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top|bottom|left|right</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10mm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.pdf</span>

- PDF 페이지 방향 설정:

`wkhtmltopdf --orientation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Landscape|Portrait</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.pdf</span>

- PDF 문서를 그레이스케일로 생성:

`wkhtmltopdf --grayscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.pdf</span>
