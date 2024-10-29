---
layout: page
title: common/pdflatex (한국어)
description: "LaTeX 소스 파일을 PDF 문서로 컴파일."
content_hash: 75055841d8ce514685c5134faa58a6851ca54314
last_modified_at: 2024-10-29
related_topics:
  - title: Deutsch version
    url: /de/common/pdflatex.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pdflatex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdflatex

LaTeX 소스 파일을 PDF 문서로 컴파일.
더 많은 정보: <https://manned.org/pdflatex>.

- PDF 문서 컴파일:

`pdflatex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>

- 출력 디렉토리를 지정하여 PDF 문서 컴파일:

`pdflatex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>

- 각 오류에서 중지하며 PDF 문서 컴파일:

`pdflatex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>
