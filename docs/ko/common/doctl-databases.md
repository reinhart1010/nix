---
layout: page
title: common/doctl-databases (한국어)
description: "MySQL, Redis, PostgreSQL 및 MongoDB 데이터베이스 서비스를 관리."
content_hash: 2e91a09d27e39027aa595c2bec91bde91e0568b6
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/doctl-databases.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doctl databases

MySQL, Redis, PostgreSQL 및 MongoDB 데이터베이스 서비스를 관리.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases>.

- 액세스 토큰을 사용하여 `doctl databases` 명령을 실행:

`doctl databases `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">액세스_토큰</span>

- 데이터베이스 클러스터에 대한 세부 정보를 가져옴:

`doctl databases get`

- 데이터베이스 클러스터를 나열:

`doctl databases list`

- 데이터베이스 클러스터 생성:

`doctl databases create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 클러스터 삭제:

`doctl databases delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>
