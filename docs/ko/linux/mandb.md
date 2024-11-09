---
layout: page
title: linux/mandb (한국어)
description: "사전 형식화된 매뉴얼 페이지 데이터베이스 관리."
content_hash: 522646de06672c4d31b227556172fe82ab5464d9
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mandb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mandb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mandb

사전 형식화된 매뉴얼 페이지 데이터베이스 관리.
더 많은 정보: <https://manned.org/mandb>.

- 매뉴얼 페이지 정리 및 처리:

`mandb`

- 단일 항목 업데이트:

`mandb --filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 업데이트 대신 처음부터 항목 생성:

`mandb --create`

- 사용자 데이터베이스만 처리:

`mandb --user-db`

- 오래된 항목을 정리하지 않음:

`mandb --no-purge`

- 매뉴얼 페이지의 유효성 검사:

`mandb --test`
