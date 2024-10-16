---
layout: page
title: common/eslint (한국어)
description: "JavaScript 및 JSX용 플러그형 린팅 유틸리티."
content_hash: 292665030a51b2185bea457d5fdfa6cb3fdd5bdf
last_modified_at: 2024-10-16
related_topics:
  - title: Deutsch version
    url: /de/common/eslint.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/eslint.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/eslint.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/eslint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/eslint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eslint

JavaScript 및 JSX용 플러그형 린팅 유틸리티.
더 많은 정보: <https://eslint.org>.

- ESLint 구성파일 생성:

`eslint --init`

- 하나 이상의 파일 린팅:

`eslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.js 경로/대상/파일2.js ...</span>

- 린트 문제 수정:

`eslint --fix`

- 지정된 구성 파일을 사용하는 린트:

`eslint -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.js 경로/대상/파일2.js</span>
