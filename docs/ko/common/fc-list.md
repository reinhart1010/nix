---
layout: page
title: common/fc-list (한국어)
description: "시스템에 설치된 사용 가능한 글꼴을 나열."
content_hash: 9ca5bd467aa367105acab768c49dcee24e556be7
last_modified_at: 2025-01-05
related_topics:
  - title: English version
    url: /en/common/fc-list.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/fc-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fc-list.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/fc-list.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fc-list

시스템에 설치된 사용 가능한 글꼴을 나열.
더 많은 정보: <https://manned.org/fc-list>.

- 시스템에 설치된 글꼴 목록을 반환:

`fc-list`

- 주어진 이름으로 설치된 글꼴 목록을 반환:

`fc-list | grep '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DejaVu Serif</span>`'`

- 시스템에 설치된 글꼴 수를 반환:

`fc-list | wc -l`
