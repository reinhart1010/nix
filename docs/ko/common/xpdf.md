---
layout: page
title: common/xpdf (한국어)
description: "Portable Document Format (PDF) 파일 뷰어."
content_hash: aa4decdaba801536da22276f6eff69dd025a64ac
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/xpdf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xpdf

Portable Document Format (PDF) 파일 뷰어.
더 많은 정보: <https://www.xpdfreader.com/xpdf-man.html>.

- PDF 파일 열기:

`xpdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- 특정 페이지에서 PDF 파일 열기:

`xpdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_번호</span>

- 압축된 PDF 파일 열기:

`xpdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf.tar</span>

- 전체 화면 모드로 PDF 파일 열기:

`xpdf -fullscreen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- 초기 줌 비율 지정:

`xpdf -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">75</span>`% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- 페이지 너비 또는 전체 페이지로 초기 줌 비율 지정:

`xpdf -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page|width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>
