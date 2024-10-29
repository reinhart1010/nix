---
layout: page
title: linux/pdftohtml (한국어)
description: "PDF 파일을 HTML, XML 및 PNG 이미지로 변환."
content_hash: cf9548e68ebf58afe93f6e247e8c9908d6cbd912
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/pdftohtml.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdftohtml

PDF 파일을 HTML, XML 및 PNG 이미지로 변환.
더 많은 정보: <https://manned.org/pdftohtml>.

- PDF 파일을 HTML 파일로 변환:

`pdftohtml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.html</span>

- PDF 파일에서 이미지를 무시:

`pdftohtml -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.html</span>

- 모든 PDF 페이지를 포함하는 단일 HTML 파일 생성:

`pdftohtml -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.html</span>

- PDF 파일을 XML 파일로 변환:

`pdftohtml -xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.xml</span>
