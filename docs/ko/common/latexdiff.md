---
layout: page
title: common/latexdiff (한국어)
description: "두 개의 LaTeX 파일 간의 차이점을 확인."
content_hash: 560aef7885624fe75805dbe59e1867c00b8a3728
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/latexdiff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/latexdiff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># latexdiff

두 개의 LaTeX 파일 간의 차이점을 확인.
더 많은 정보: <https://ctan.org/pkg/latexdiff>.

- 서로 다른 버전의 LaTeX 파일 간의 변경 사항 확인 (결과 LaTeX 파일은 밑줄로 차이점을 표시하도록 컴파일 가능):

`latexdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오래된.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새.tex</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">차이.tex</span>

- 서로 다른 버전의 LaTeX 파일 간의 변경 사항을 굵은 글씨로 강조하여 확인:

`latexdiff --type=BOLD `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오래된.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새.tex</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">차이.tex</span>

- 서로 다른 버전의 LaTeX 파일 간의 변경 사항을 확인하고, 방정식의 작은 변경 사항을 추가 및 삭제된 그래픽과 함께 표시:

`latexdiff --math-markup=fine --graphics-markup=both `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오래된.tex</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새.tex</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">차이.tex</span>
