---
layout: page
title: common/pgbench (한국어)
description: "PostgreSQL에 대한 벤치마크 테스트 실행."
content_hash: 3b287949350deb719a65cd90e9e1f1988f4630f2
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pgbench.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pgbench.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pgbench

PostgreSQL에 대한 벤치마크 테스트 실행.
더 많은 정보: <https://www.postgresql.org/docs/10/pgbench.html>.

- 기본 크기의 50배로 데이터베이스 초기화:

`pgbench --initialize --scale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 10명의 클라이언트, 2개의 작업 스레드, 클라이언트당 10,000개의 트랜잭션으로 데이터베이스 벤치마크 실행:

`pgbench --client=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --transactions=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>
