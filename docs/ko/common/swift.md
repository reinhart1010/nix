---
layout: page
title: common/swift (한국어)
description: "Swift 프로젝트를 생성, 실행 및 빌드."
content_hash: cbcf0cac60e01576e00bdd0fb44d13411002b324
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/swift.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/swift.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># swift

Swift 프로젝트를 생성, 실행 및 빌드.
더 많은 정보: <https://swift.org>.

- REPL(대화형 셸) 시작:

`swift repl`

- 프로그램 실행:

`swift `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.swift</span>

- 패키지 관리자로 새 프로젝트 시작:

`swift package init`

- Xcode 프로젝트 파일 생성:

`swift package generate-xcodeproj`

- 의존성 업데이트:

`swift package update`

- 프로젝트를 릴리스용으로 컴파일:

`swift build -c release`
