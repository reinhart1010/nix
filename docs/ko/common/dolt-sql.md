---
layout: page
title: common/dolt-sql (한국어)
description: "SQL 쿼리를 실행. 여러 SQL 문은 세미콜론으로 구분해야 함."
content_hash: a068e6f7ad48df0e5bbafb46ff9ea92eca337867
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/dolt-sql.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dolt-sql.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dolt sql

SQL 쿼리를 실행. 여러 SQL 문은 세미콜론으로 구분해야 함.
더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-sql>.

- 단일 쿼리 실행:

`dolt sql --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INSERT INTO t values (1, 3);</span>`"`

- 저장된 모든 쿼리를 나열:

`dolt sql --list-saved`
