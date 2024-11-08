---
layout: page
title: common/initdb (한국어)
description: "디스크에 PostgreSQL 데이터베이스를 생성."
content_hash: 2c2f0867305b6ab72490c5171646c4c119bba0ea
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/initdb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/initdb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># initdb

디스크에 PostgreSQL 데이터베이스를 생성.
더 많은 정보: <https://www.postgresql.org/docs/9.5/app-initdb.html>.

- `/usr/local/var/postgres`에 데이터베이스를 생성:

`initdb -D /usr/local/var/postgres`
