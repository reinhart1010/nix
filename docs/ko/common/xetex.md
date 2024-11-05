---
layout: page
title: common/xetex (한국어)
description: "XeTeX 소스 파일에서 PDF 문서를 컴파일."
content_hash: 627a8a79ccf39507f3201d4ccd0fce8ca928c991
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xetex.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xetex.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xetex

XeTeX 소스 파일에서 PDF 문서를 컴파일.
더 많은 정보: <https://www.tug.org/xetex/>.

- PDF 문서 컴파일:

`xetex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>

- 출력 디렉토리를 지정하여 PDF 문서 컴파일:

`xetex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>

- 오류 발생 시 종료하며 PDF 문서 컴파일:

`xetex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스.tex</span>
