---
layout: page
title: common/pygmentize (한국어)
description: "Python 기반의 문법 하이라이터."
content_hash: 3b9131c44119400f856109c2cf924268529b9603
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pygmentize.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pygmentize.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pygmentize

Python 기반의 문법 하이라이터.
더 많은 정보: <https://pygments.org/docs/cmdline/>.

- 파일의 문법을 하이라이트하여 `stdout`에 출력 (파일 확장자로 언어 추론):

`pygmentize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.py</span>

- 문법 하이라이트를 위한 언어를 명시적으로 설정:

`pygmentize -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자바스크립트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- 사용 가능한 렉서(입력 언어 처리기) 목록 표시:

`pygmentize -L lexers`

- 출력 파일을 HTML 형식으로 저장:

`pygmentize -f html -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일.py</span>

- 사용 가능한 출력 형식 목록 표시:

`pygmentize -L formatters`

- 추가 포매터 옵션을 사용하여 HTML 파일 출력 (전체 페이지, 줄 번호 포함):

`pygmentize -f html -O "full,linenos=True" -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>
