---
layout: page
title: common/latexmk (한국어)
description: "LaTeX 소스 파일을 완성된 문서로 컴파일."
content_hash: abbc738e08614d0a696cc6b1d597ff3467566130
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/latexmk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/latexmk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># latexmk

LaTeX 소스 파일을 완성된 문서로 컴파일.
필요에 따라 자동으로 여러 번 실행.
더 많은 정보: <https://mg.readthedocs.io/latexmk.html>.

- 모든 소스에서 DVI(장치 독립 파일) 문서 컴파일:

`latexmk`

- 특정 소스 파일에서 DVI 문서 컴파일:

`latexmk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.tex</span>

- PDF 문서 컴파일:

`latexmk -pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.tex</span>

- 문서를 뷰어에서 열고 소스 파일이 변경될 때마다 지속적으로 업데이트:

`latexmk -pvc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.tex</span>

- 오류가 있어도 문서 생성을 강제:

`latexmk -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.tex</span>

- 특정 TEX 파일에 대해 생성된 임시 TEX 파일 정리:

`latexmk -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.tex</span>

- 현재 디렉토리의 모든 임시 TEX 파일 정리:

`latexmk -c`
