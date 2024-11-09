---
layout: page
title: common/sequelize (한국어)
description: "Postgres, MySQL, MariaDB, SQLite 및 Microsoft SQL Server를 위한 Promise 기반 Node.js ORM."
content_hash: e177f81a9fbb574530754a967088993a7b260a37
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sequelize.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sequelize.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sequelize

Postgres, MySQL, MariaDB, SQLite 및 Microsoft SQL Server를 위한 Promise 기반 Node.js ORM.
더 많은 정보: <https://sequelize.org/>.

- 3개의 필드와 마이그레이션 파일로 모델 생성:

`sequelize model:generate --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>` --attributes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field1:integer,field2:string,field3:boolean</span>

- 마이그레이션 파일 실행:

`sequelize db:migrate`

- 모든 마이그레이션 되돌리기:

`sequelize db:migrate:undo:all`

- 데이터베이스를 채우기 위해 지정된 이름의 시드 파일 생성:

`sequelize seed:generate --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시드_파일_이름</span>

- 모든 시드 파일을 사용하여 데이터베이스 채우기:

`sequelize db:seed:all`
