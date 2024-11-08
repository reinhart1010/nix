---
layout: page
title: common/pg_restore (한국어)
description: "pg_dump로 생성된 아카이브 파일에서 PostgreSQL 데이터베이스 복원."
content_hash: 99889c20e444a596b6325be3706c35041e824aa9
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pg_restore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pg_restore

pg_dump로 생성된 아카이브 파일에서 PostgreSQL 데이터베이스 복원.
더 많은 정보: <https://www.postgresql.org/docs/current/app-pgrestore.html>.

- 기존 데이터베이스에 아카이브 복원:

`pg_restore -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브_파일.dump</span>

- 위와 동일하며, 사용자 이름 커스터마이즈:

`pg_restore -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브_파일.dump</span>

- 위와 동일하며, 호스트 및 포트 커스터마이즈:

`pg_restore -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브_파일.dump</span>

- 아카이브에 포함된 데이터베이스 객체 목록:

`pg_restore --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브_파일.dump</span>

- 데이터베이스 객체를 생성하기 전에 삭제:

`pg_restore --clean -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브_파일.dump</span>

- 여러 작업을 사용하여 복원:

`pg_restore -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브_파일.dump</span>
