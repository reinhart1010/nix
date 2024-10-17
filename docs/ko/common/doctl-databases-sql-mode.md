---
layout: page
title: common/doctl-databases-sql-mode (한국어)
description: "MySQL 데이터베이스 클러스터의 전역 SQL 모드를 보고 구성."
content_hash: 27aaa371dfbac9c4a509ab5b8cb667b8c6e56250
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/doctl-databases-sql-mode.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doctl databases sql-mode

MySQL 데이터베이스 클러스터의 전역 SQL 모드를 보고 구성.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/sql-mode/>.

- 액세스 토큰을 사용하여 `doctl databases sql-mode` 명령을 실행:

`doctl databases sql-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">액세스_토큰</span>

- MySQL 데이터베이스 클러스터의 SQL 모드를 가져옴:

`doctl databases sql-mode get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>

- MySQL 데이터베이스 클러스터의 SQL 모드를 지정된 모드로 덮어씀:

`doctl databases sql-mode set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sql_모드_1 sql_모드_2 ...</span>
