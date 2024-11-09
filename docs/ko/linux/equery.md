---
layout: page
title: linux/equery (한국어)
description: "Portage 패키지에 대한 정보를 표시합니다."
content_hash: 4cafeea8556e1bb54d223d0dc0b54f84edb454c9
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/equery.html
    icon: bi bi-globe
tldri18n_status: 2
---
# equery

Portage 패키지에 대한 정보를 표시합니다.
더 많은 정보: <https://wiki.gentoo.org/wiki/Equery>.

- 설치된 모든 패키지 나열:

`equery list '*'`

- 포티지 트리와 오버레이에서 설치된 패키지를 검색:

`equery list -po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 특정 패키지에 의존하는 모든 패키지 나열:

`equery depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 패키지가 의존하는 모든 패키지 나열:

`equery depgraph `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지가 설치한 모든 파일 나열:

`equery files --tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
