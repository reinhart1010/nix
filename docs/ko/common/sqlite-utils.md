---
layout: page
title: common/sqlite-utils (한국어)
description: "SQLite 데이터베이스를 다양한 방식으로 조작하기 위한 명령줄 도구."
content_hash: 35b8804342a5c54546eb31ccc97016188f54fd45
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/sqlite-utils.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sqlite-utils

SQLite 데이터베이스를 다양한 방식으로 조작하기 위한 명령줄 도구.
더 많은 정보: <https://sqlite-utils.datasette.io/en/stable/cli.html>.

- 데이터베이스 생성:

`sqlite-utils create-database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/database.db</span>

- 테이블 생성:

`sqlite-utils create-table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/database.db</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id integer name text height float photo blob --pk id</span>

- 테이블 목록:

`sqlite-utils tables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/database.db</span>

- 레코드 삽입 또는 업데이트:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo '[ {"id": 1, "name": "Linus Torvalds"}, {"id": 2, "name": "Steve Wozniak"}, {"id": 3, "name": "Tony Hoare"} ]'</span>` | sqlite-utils upsert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/database.db</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>` - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--pk id</span>

- 레코드 선택:

`sqlite-utils rows `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/database.db</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>

- 레코드 삭제:

`sqlite-utils query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/database.db</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delete from table_name where name = 'Tony Hoare'</span>`"`

- 테이블 삭제:

`sqlite-utils drop-table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/database.db</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>

- 도움말 표시:

`sqlite-utils -h`
