---
layout: page
title: common/doctl-databases-pool (한국어)
description: "데이터베이스 클러스터의 연결 풀을 관리."
content_hash: ea7e415096e054562a6ecb57dee529156806934d
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/doctl-databases-pool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doctl-databases-pool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doctl databases pool

데이터베이스 클러스터의 연결 풀을 관리.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/pool/>.

- 액세스 토큰을 사용하여 `doctl databases pool` 명령을 실행:

`doctl databases pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">액세스_토큰</span>

- 데이터베이스 연결 풀에 대한 정보 검색:

`doctl databases pool get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름</span>

- 데이터베이스 클러스터에 대한 연결 풀을 나열:

`doctl databases pool list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>

- 데이터베이스에 대한 연결 풀을 생성:

`doctl databases pool create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름</span>` --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_풀_이름</span>` --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_크기</span>

- 데이터베이스에 대한 연결 풀을 삭제:

`doctl databases pool create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름</span>
