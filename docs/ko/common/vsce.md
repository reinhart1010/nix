---
layout: page
title: common/vsce (한국어)
description: "Visual Studio Code 확장 관리자."
content_hash: d81e7eeca1496b429b77c555aebf35029292204f
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/vsce.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vsce.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vsce

Visual Studio Code 확장 관리자.
더 많은 정보: <https://github.com/microsoft/vscode-vsce>.

- 특정 게시자가 만든 모든 확장 나열:

`vsce list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게시자</span>

- 확장을 주 버전, 부 버전 또는 패치 버전으로 게시:

`vsce publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">major|minor|patch</span>

- 확장 취소 게시:

`vsce unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장_ID</span>

- 현재 작업 디렉토리를 `.vsix` 파일로 패키징:

`vsce package`

- 확장과 관련된 메타데이터 표시:

`vsce show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장_ID</span>
