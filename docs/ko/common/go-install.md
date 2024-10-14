---
layout: page
title: common/go-install (한국어)
description: "import 경로로 지정된 패키지를 컴파일하고 설치."
content_hash: 4e8fa97823bb1118154abb3ec349712aae795e78
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/go-install.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-install.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/go-install.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># go install

import 경로로 지정된 패키지를 컴파일하고 설치.
더 많은 정보: <https://pkg.go.dev/cmd/go#hdr-Compile_and_install_packages_and_dependencies>.

- 현재 패키지를 컴파일하고 설치:

`go install`

- 특정 로컬 패키지를 컴파일하고 설치:

`go install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지</span>

- 현재 디렉토리의 `go.mod`를 무시하고 프로그램의 최신 버전 설치:

`go install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">golang.org/x/tools/gopls</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최신</span>

- 현재 디렉토리의 `go.mod`에 의해 선택된 버전으로 프로그램 설치:

`go install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">golang.org/x/tools/gopls</span>
