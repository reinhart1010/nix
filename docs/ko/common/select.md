---
layout: page
title: common/select (한국어)
description: "메뉴를 생성하기 위한 Bash 내장 구조."
content_hash: 7c61982c1d790ef91274f59b81493361947a2ad9
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/select.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/select.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># select

메뉴를 생성하기 위한 Bash 내장 구조.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-select>.

- 개별 단어로 메뉴 생성:

`select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단어</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사과 오렌지 배 바나나</span>`; do echo $`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단어</span>`; done`

- 다른 명령의 출력으로 메뉴 생성:

`select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">줄</span>` in $(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>`); do echo $`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">줄</span>`; done`

- `select`의 프롬프트 문자열을 지정하고 현재 디렉토리에서 파일이나 폴더를 선택하는 메뉴 생성:

`PS3="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일을 선택하세요: </span>`"; select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>` in *; do echo $`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>`; done`

- Bash 배열로 메뉴 생성:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">과일들</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사과 오렌지 배 바나나</span>`); select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단어</span>` in $`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{과일들[@]}</span>`; do echo $`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단어</span>`; done`
