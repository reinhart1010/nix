---
layout: page
title: common/csvsql (한국어)
description: "CSV 파일에 대한 SQL문을 생성하거나 해당 문을 데이터베이스에서 직접 실행."
content_hash: a30b010dbaedeefb4e04a20ec10bc75eb8073b83
last_modified_at: 2024-10-12
related_topics:
  - title: Deutsch version
    url: /de/common/csvsql.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/csvsql.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csvsql

CSV 파일에 대한 SQL문을 생성하거나 해당 문을 데이터베이스에서 직접 실행.
csvkit에 포함됨.
더 많은 정보: <https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html>.

- CSV 파일에 대한 `CREATE TABLE` SQL 문을 생성:

`csvsql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터.csv</span>

- CSV 파일을 SQL 데이터베이스로 가져옴:

`csvsql --insert --db "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql://user:password@host/database</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- CSV 파일에서 SQL 쿼리를 실행:

`csvsql --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">select * from 'data'</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>
