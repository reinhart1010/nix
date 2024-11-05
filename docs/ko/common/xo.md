---
layout: page
title: common/xo (한국어)
description: "JavaScript용 플러그인 가능하고 설정이 필요 없는 린트 유틸리티."
content_hash: 445b480c7b9a2db7b8d4b0e235e45ff9357de859
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xo

JavaScript용 플러그인 가능하고 설정이 필요 없는 린트 유틸리티.
더 많은 정보: <https://github.com/xojs/xo>.

- "src" 폴더의 파일을 린트:

`xo`

- 주어진 파일 세트를 린트:

`xo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.js 경로/대상/파일2.js ...</span>

- 발견된 린트 문제를 자동으로 수정:

`xo --fix`

- 탭 대신 공백을 들여쓰기로 사용하여 린트:

`xo --space`

- "prettier" 코드 스타일로 린트:

`xo --prettier`
