---
layout: page
title: common/pg_dump (한국어)
description: "PostgreSQL 데이터베이스를 스크립트 파일 또는 다른 아카이브 파일로 추출."
content_hash: 2c3d8a98fd51fd3bdf9a78fe0aef0a10214c61e7
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pg_dump.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pg_dump.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pg_dump

PostgreSQL 데이터베이스를 스크립트 파일 또는 다른 아카이브 파일로 추출.
더 많은 정보: <https://www.postgresql.org/docs/current/app-pgdump.html>.

- 데이터베이스를 SQL 스크립트 파일로 덤프:

`pg_dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DB_이름</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일.sql</span>

- 위와 동일하게, 사용자 이름을 지정:

`pg_dump -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DB_이름</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일.sql</span>

- 위와 동일하게, 호스트 및 포트를 지정:

`pg_dump -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DB_이름</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일.sql</span>

- 데이터베이스를 사용자 정의 형식의 아카이브 파일로 덤프:

`pg_dump -Fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DB_이름</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일.dump</span>

- 데이터베이스 데이터만 SQL 스크립트 파일로 덤프:

`pg_dump -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DB_이름</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.sql</span>

- 스키마(데이터 정의)만 SQL 스크립트 파일로 덤프:

`pg_dump -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DB_이름</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.sql</span>
