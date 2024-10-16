---
layout: page
title: common/doctl-databases-sql-mode (한국어)
description: "MySQL 데이터베이스 클러스터의 전역 SQL 모드를 보고 구성."
content_hash: 27aaa371dfbac9c4a509ab5b8cb667b8c6e56250
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/doctl-databases-sql-mode.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doctl-databases-sql-mode.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doctl databases sql-mode

MySQL 데이터베이스 클러스터의 전역 SQL 모드를 보고 구성.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/databases/sql-mode/>.

- 액세스 토큰을 사용하여 `doctl databases sql-mode` 명령을 실행:

`doctl databases sql-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">액세스_토큰</span>

- MySQL 데이터베이스 클러스터의 SQL 모드를 가져옴:

`doctl databases sql-mode get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>

- MySQL 데이터베이스 클러스터의 SQL 모드를 지정된 모드로 덮어씀:

`doctl databases sql-mode set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sql_모드_1 sql_모드_2 ...</span>
