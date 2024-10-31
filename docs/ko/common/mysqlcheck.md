---
layout: page
title: common/mysqlcheck (한국어)
description: "MySQL 테이블 검사 및 복구."
content_hash: cb9c1e0824c16118e3ee2edbbe20ecb1dc8ad302
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/mysqlcheck.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mysqlcheck.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mysqlcheck

MySQL 테이블 검사 및 복구.
더 많은 정보: <https://dev.mysql.com/doc/refman/8.0/en/mysqlcheck.html>.

- 테이블 검사:

`mysqlcheck --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블</span>

- 테이블을 검사하고 접근을 위한 인증 정보 제공:

`mysqlcheck --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 테이블 복구:

`mysqlcheck --repair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블</span>

- 테이블 최적화:

`mysqlcheck --optimize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블</span>
