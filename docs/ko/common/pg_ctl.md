---
layout: page
title: common/pg_ctl (한국어)
description: "PostgreSQL 서버 및 데이터베이스 클러스터를 제어하는 유틸리티."
content_hash: 8735fdb69dd9c3c558fea391b9395a542f94fbc3
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pg_ctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pg_ctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pg_ctl

PostgreSQL 서버 및 데이터베이스 클러스터를 제어하는 유틸리티.
더 많은 정보: <https://www.postgresql.org/docs/current/app-pg-ctl.html>.

- 새로운 PostgreSQL 데이터베이스 클러스터 초기화:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터_디렉토리</span>` init`

- PostgreSQL 서버 시작:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터_디렉토리</span>` start`

- PostgreSQL 서버 중지:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터_디렉토리</span>` stop`

- PostgreSQL 서버 재시작:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터_디렉토리</span>` restart`

- PostgreSQL 서버 설정 다시 로드:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터_디렉토리</span>` reload`
