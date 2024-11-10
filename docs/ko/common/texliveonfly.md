---
layout: page
title: common/texliveonfly (한국어)
description: "`.tex` 파일을 컴파일하는 동안 누락된 TeX Live 패키지를 다운로드."
content_hash: 7a328b9b43cec0f11262a72ad908f6bb40090d18
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/common/texliveonfly.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/texliveonfly.html
    icon: bi bi-globe
tldri18n_status: 2
---
# texliveonfly

`.tex` 파일을 컴파일하는 동안 누락된 TeX Live 패키지를 다운로드.
더 많은 정보: <https://ctan.org/pkg/texliveonfly>.

- 컴파일하는 동안 누락된 패키지 다운로드:

`texliveonfly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>

- 특정 컴파일러 사용 (`pdflatex`가 기본값):

`texliveonfly --compiler=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컴파일러</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>

- 사용자 지정 TeX Live `bin` 폴더 사용:

`texliveonfly --texlive_bin=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/texlive_bin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>
