---
layout: page
title: common/pup (한국어)
description: "명령줄 HTML 파싱 도구."
content_hash: cfb98094f8b79a176774b3060ba43b4fe67859e0
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pup

명령줄 HTML 파싱 도구.
더 많은 정보: <https://github.com/ericchiang/pup>.

- 원시 HTML 파일을 정리되고 들여쓰기된 색상 형식으로 변환:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup --color`

- 요소 태그 이름으로 HTML 필터링:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>`'`

- ID로 HTML 필터링:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">div#아이디</span>`'`

- 속성 값으로 HTML 필터링:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input[type="text"]</span>`'`

- 필터링된 HTML 요소와 그 자식 요소의 모든 텍스트 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">div</span>` text{}'`

- HTML을 JSON으로 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">div</span>` json{}'`
