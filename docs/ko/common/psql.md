---
layout: page
title: common/psql (한국어)
description: "PostgreSQL 명령줄 클라이언트."
content_hash: c0da854e53e814ad37e2cf8a0494eaa0162021ee
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/psql.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/psql.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># psql

PostgreSQL 명령줄 클라이언트.
더 많은 정보: <https://www.postgresql.org/docs/current/app-psql.html>.

- 데이터베이스에 연결. 기본적으로, 현재 로그인한 사용자로 포트 5432를 사용하여 로컬 소켓에 연결:

`psql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스</span>

- 주어진 서버 호스트에서 주어진 포트로 주어진 사용자 명으로 데이터베이스에 연결, 비밀번호 입력은 생략:

`psql -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스</span>

- 데이터베이스에 연결; 사용자는 비밀번호를 입력해야 함:

`psql -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스</span>

- 주어진 데이터베이스에서 단일 SQL 쿼리 또는 PostgreSQL 명령 실행 (쉘 스크립트에 유용):

`psql -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스</span>

- 주어진 데이터베이스에서 파일로부터 명령 실행:

`psql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.sql</span>
