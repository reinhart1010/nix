---
layout: page
title: common/doctl-databases-options (한국어)
description: "각 데이터베이스 엔진에서 사용 가능한 옵션 탐색을 활성화."
content_hash: 1e3c151e4d765f4f61cf028e99758b09b38961bc
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/doctl-databases-options.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doctl databases options

각 데이터베이스 엔진에서 사용 가능한 옵션 탐색을 활성화.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/options>.

- 액세스 토큰을 사용하여 `doctl databases options` 명령을 실행:

`doctl databases options `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">액세스_토큰</span>

- 사용 가능한 데이터베이스 엔진 목록을 검색:

`doctl databases options engines`

- 특정 데이터베이스 엔진에 사용 가능한 지역 목록을 검색:

`doctl databases options regions --engine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pg|mysql|redis|mongodb</span>

- 특정 데이터베이스 엔진에 사용 가능한 슬러그 목록을 검색:

`doctl databases options slugs --engine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pg|mysql|redis|mongodb</span>

- 특정 데이터베이스 엔진에 사용 가능한 버전 목록을 검색:

`doctl databases options versions --engine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pg|mysql|redis|mongodb</span>
