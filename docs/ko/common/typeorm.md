---
layout: page
title: common/typeorm (한국어)
description: "Node.js, 브라우저, Cordova, Ionic, React Native, NativeScript, Electron 플랫폼에서 실행할 수 있는 JavaScript ORM."
content_hash: 949f051bfb579971122bf016d29f48a837e07d05
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/typeorm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# typeorm

Node.js, 브라우저, Cordova, Ionic, React Native, NativeScript, Electron 플랫폼에서 실행할 수 있는 JavaScript ORM.
더 많은 정보: <https://typeorm.io/>.

- 새로운 TypeORM 프로젝트 구조 생성:

`typeorm init`

- 빈 마이그레이션 파일 생성:

`typeorm migration:create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마이그레이션_이름</span>

- 스키마를 업데이트하는 SQL 문이 포함된 마이그레이션 파일 생성:

`typeorm migration:generate --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마이그레이션_이름</span>

- 대기 중인 모든 마이그레이션 실행:

`typeorm migration:run`

- 특정 디렉터리에 새 엔터티 파일 생성:

`typeorm entity:create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">엔터티</span>` --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 기본 연결에서 `typeorm schema:sync`로 실행될 SQL 문 표시:

`typeorm schema:log`

- 기본 연결에서 특정 SQL 문 실행:

`typeorm query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sql_문장</span>

- 하위 명령에 대한 도움말 표시:

`typeorm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>` --help`
