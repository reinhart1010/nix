---
layout: page
title: common/latex (한국어)
description: "LaTeX 소스 파일에서 DVI 문서를 컴파일합니다."
content_hash: cf92f68d9c0ca4e9787260157b1cbf520fc4e830
last_modified_at: 2024-11-07
related_topics:
  - title: Deutsch version
    url: /de/common/latex.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/latex.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/latex.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/latex.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># latex

LaTeX 소스 파일에서 DVI 문서를 컴파일합니다.
더 많은 정보: <https://www.latex-project.org>.

- DVI 문서 컴파일:

`latex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>

- 출력 디렉토리를 지정하여 DVI 문서 컴파일:

`latex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>

- 각 오류 발생 시 종료하며 DVI 문서 컴파일:

`latex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>
