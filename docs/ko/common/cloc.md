---
layout: page
title: common/cloc (한국어)
description: "소스코드와 주석의 줄 개수를 세고 차이를 계산합니다."
content_hash: 567e7c646c4f22d87a5134c8f597732d8ea20b07
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cloc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cloc.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cloc

소스코드와 주석의 줄 개수를 세고 차이를 계산합니다.
더 많은 정보: <https://github.com/AlDanial/cloc>.

- 디렉토리 안의 모든 코드의 줄 개수를 셉니다:

`cloc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/디렉토리</span>

- 진행 바로 현재 진행 중인 과정을 보여주면서 디렉토리 안의 모든 코드의 줄 개수를 셉니다:

`cloc --progress=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/디렉토리</span>

- 두 개의 디렉토리 구조를 비교하고 차이의 개수를 셉니다:

`cloc --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/디렉토리/첫번째</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/디렉토리/두번째</span>
