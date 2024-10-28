---
layout: page
title: common/pdftex (한국어)
description: "TeX 소스 파일에서 PDF 문서를 컴파일."
content_hash: 57117b5d29987eac1d22184f238bbc3af6d629f2
last_modified_at: 2024-10-28
related_topics:
  - title: Deutsch version
    url: /de/common/pdftex.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pdftex.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pdftex.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pdftex

TeX 소스 파일에서 PDF 문서를 컴파일.
더 많은 정보: <https://www.tug.org/applications/pdftex/>.

- PDF 문서 컴파일:

`pdftex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>

- 출력 폴더를 지정하여 PDF 문서 컴파일:

`pdftex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>

- 각 오류 발생 시 종료하며 PDF 문서 컴파일:

`pdftex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>
