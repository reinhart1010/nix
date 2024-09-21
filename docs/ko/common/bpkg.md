---
layout: page
title: common/bpkg (한국어)
description: "Bash 스크립트용 패키지 관리자."
content_hash: 1022972004dfe6141d1d6212666f64b26839a09e
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/bpkg.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bpkg.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/bpkg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bpkg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bpkg

Bash 스크립트용 패키지 관리자.
더 많은 정보: <https://github.com/bpkg/bpkg>.

- 로컬 색인 업데이트:

`bpkg update`

- 전역적으로 패키지를 설치:

`bpkg install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 현재 디렉터리의 하위 디렉터리에 패키지를 설치:

`bpkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 버전의 패키지를 전역적으로 설치:

`bpkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>` -g`

- 특정 패키지에 대한 세부정보 표시:

`bpkg show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 선택적으로 인수를 지정하여, 명령을 실행:

`bpkg run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인자1 인자2 ...</span>
