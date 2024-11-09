---
layout: page
title: common/standard (한국어)
description: "JavaScript 코드의 린트 및 수정을 위한 JavaScript Standard Style 도구."
content_hash: dbae955dad923753c06e3ea6aeb867a4a5a38bd2
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/standard.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/standard.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># standard

JavaScript 코드의 린트 및 수정을 위한 JavaScript Standard Style 도구.
더 많은 정보: <https://standardjs.com>.

- 현재 디렉토리의 모든 JavaScript 소스 파일을 린트:

`standard`

- 특정 JavaScript 파일(들)을 린트:

`standard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 린트 시 자동 수정 적용:

`standard --fix`

- 사용 가능한 전역 변수 선언:

`standard --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>

- 린트 시 사용자 지정 ESLint 플러그인 사용:

`standard --plugin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인</span>

- 린트 시 사용자 지정 JS 파서 사용:

`standard --parser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파서</span>

- 린트 시 사용자 지정 ESLint 환경 사용:

`standard --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경</span>
