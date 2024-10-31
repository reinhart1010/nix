---
layout: page
title: common/sqlite3 (한국어)
description: "SQLite 3의 명령줄 인터페이스로, 자체 포함 파일 기반 임베디드 SQL 엔진입니다."
content_hash: 93c53efcc4f5af993c1a67ef7a5d54d8e7720ac6
last_modified_at: 2024-10-31
related_topics:
  - title: Deutsch version
    url: /de/common/sqlite3.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sqlite3.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sqlite3.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sqlite3

SQLite 3의 명령줄 인터페이스로, 자체 포함 파일 기반 임베디드 SQL 엔진입니다.
더 많은 정보: <https://sqlite.org>.

- 새 데이터베이스로 대화형 셸 시작:

`sqlite3`

- 기존 데이터베이스로 대화형 셸 열기:

`sqlite3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터베이스.sqlite3</span>

- 데이터베이스에 SQL 문 실행 후 종료:

`sqlite3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터베이스.sqlite3</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SELECT * FROM some_table;</span>`'`
