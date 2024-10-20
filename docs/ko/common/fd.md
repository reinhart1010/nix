---
layout: page
title: common/fd (한국어)
description: "`find`의 대안."
content_hash: 02a8bf4a7c37aedbcaafab70675b99a99681c6f2
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fd

`find`의 대안.
`find`보다 더 빠르고 쉽게 사용하는 것을 목표.
더 많은 정보: <https://github.com/sharkdp/fd>.

- 현재 디렉터리에서 특정 패턴과 일치하는 파일을 반복적으로 찾음:

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string|regex</span>`"`

- `foo`로 시작하는 파일 찾기:

`fd "^foo"`

- 특정 확장자를 가진 파일 찾기:

`fd --extension txt`

- 특정 디렉터리에서 파일 찾기:

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string|regex</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 검색에 무시되거나 숨겨진 파일을 포함:

`fd --hidden --no-ignore "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string|regex</span>`"`

- 반환된 각 검색 결과에 대해 명령을 실행:

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string|regex</span>`" --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
