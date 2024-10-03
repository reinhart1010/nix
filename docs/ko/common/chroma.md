---
layout: page
title: common/chroma (한국어)
description: "범용 구문 강조 표시기."
content_hash: be5c1a81a1d471d7d45a9c773afb1bca60a29932
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/chroma.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/chroma.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chroma

범용 구문 강조 표시기.
`--lexer` 옵션은 파일 확장자에 따라 자동으로 결정되므로, 일반적으로 필요하지 않음.
더 많은 정보: <https://github.com/alecthomas/chroma>.

- Python 어희 분석기를 사용해 파일에서 소스 코드를 강조 표시하고 `stdout`으로 출력:

`chroma --lexer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일.py</span>

- Go 어휘 분석기를 사용하여 파일의 소스코드를 강조 표시하고 HTML 파일로 출력:

`chroma --lexer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go</span>` --formatter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일.go</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_파일.html</span>

- C++ 어휘 분석기를 사용하여 `stdin`의 소스코드를 강조표시하고, Monokai 스타일을 사용하여 SVG 파일로 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | chroma --lexer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c++</span>` --formatter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg</span>` --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monokai</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_파일.svg</span>

- 사용 가능한 어휘 분석기, 스타일 및 포맷터 목록 나열:

`chroma --list`
