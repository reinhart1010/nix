---
layout: page
title: common/mysqlcheck (한국어)
description: "MySQL 테이블 검사 및 복구."
content_hash: cb9c1e0824c16118e3ee2edbbe20ecb1dc8ad302
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/mysqlcheck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mysqlcheck

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
