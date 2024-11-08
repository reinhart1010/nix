---
layout: page
title: common/pg_dumpall (한국어)
description: "PostgreSQL 데이터베이스 클러스터를 스크립트 파일 또는 다른 아카이브 파일로 추출."
content_hash: ace8f025b741ed1ae774d323a82a2bb82292c4ad
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pg_dumpall.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pg_dumpall

PostgreSQL 데이터베이스 클러스터를 스크립트 파일 또는 다른 아카이브 파일로 추출.
더 많은 정보: <https://www.postgresql.org/docs/current/app-pg-dumpall.html>.

- 모든 데이터베이스 덤프:

`pg_dumpall > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sql</span>

- 특정 사용자 이름을 사용하여 모든 데이터베이스 덤프:

`pg_dumpall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-U|--username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sql</span>

- 위와 동일하며, 호스트와 포트 맞춤 설정:

`pg_dumpall -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일.sql</span>

- 데이터베이스 데이터를 SQL 스크립트 파일로만 덤프:

`pg_dumpall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--data-only</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sql</span>

- 스키마(데이터 정의)만 SQL 스크립트 파일로 덤프:

`pg_dumpall -s > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일.sql</span>
