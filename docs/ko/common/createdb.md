---
layout: page
title: common/createdb (한국어)
description: "PostgreSQL 데이터베이스 생성."
content_hash: 76fa10269cb4d1b810d9798e091df131820664f4
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/createdb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# createdb

PostgreSQL 데이터베이스 생성.
더 많은 정보: <https://www.postgresql.org/docs/current/app-createdb.html>.

- 현재 사용자가 가지고 있는 데이터베이스를 생성:

`createdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 설명과 함께 특정 사용자가 소유한 데이터베이스를 생성:

`createdb --owner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설명</span>`'`

- 템플릿에서 데이터베이스를 생성:

`createdb --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">템플릿_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>
