---
layout: page
title: common/tex (한국어)
description: "TeX 소스 파일에서 DVI 문서를 컴파일."
content_hash: 1a33a920c6e843fc03c4bc1903e7a37e87ad4ed5
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/common/tex.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tex

TeX 소스 파일에서 DVI 문서를 컴파일.
더 많은 정보: <https://www.tug.org/begin.html>.

- DVI 문서 컴파일:

`tex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>

- 출력 폴더를 지정하여 DVI 문서 컴파일:

`tex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>

- 각 오류 발생 시 종료하며 DVI 문서 컴파일:

`tex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>
