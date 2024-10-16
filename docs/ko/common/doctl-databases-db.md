---
layout: page
title: common/doctl-databases-db (한국어)
description: "데이터베이스 클러스터에서 제공하는 데이터베이스를 관리."
content_hash: c3a4783e7522aa434e156ce7721a00d5d840d7db
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/doctl-databases-db.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doctl-databases-db.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doctl databases db

데이터베이스 클러스터에서 제공하는 데이터베이스를 관리.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/db>.

- 액세스 토큰을 사용하여 `doctl databases db` 명령을 실행:

`doctl databases db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">액세스_토큰</span>

- 특정 데이터베이스 클러스터에서 호스팅되는 특정 데이터베이스의 이름을 검색:

`doctl databases db get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 특정 데이터베이스 클러스터 내에서 호스팅되는 기존 데이터베이스를 나열:

`doctl databases db list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>

- 주어진 데이터베이스 클러스터에 주어진 이름을 가진 데이터베이스를 생성:

`doctl databases db create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 주어진 데이터베이스 클러스터에 주어진 이름을 가진 데이터베이스를 삭제:

`doctl databases db delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>
