---
layout: page
title: common/mongo (한국어)
description: "레거시 MongoDB 셸. 새로운 셸에 대해서는 `mongosh`를 참조."
content_hash: fdd542347424a460c66fafb1c6c5d6b61d26c595
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/mongo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/mongo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mongo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mongo

레거시 MongoDB 셸. 새로운 셸에 대해서는 `mongosh`를 참조.
참고: 모든 연결 옵션은 하나의 문자열로 대체할 수 있습니다: `mongodb://user@host:port/db_name?authSource=authdb_name`.
더 많은 정보: <https://docs.mongodb.com/manual/reference/program/mongo>.

- 기본 포트(`mongodb://localhost:27017`)에서 로컬 데이터베이스에 연결:

`mongo`

- 데이터베이스에 연결:

`mongo --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 지정된 데이터베이스에서 지정된 사용자 명으로 인증(비밀번호 입력이 필요합니다):

`mongo --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --authenticationDatabase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인증_데이터베이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 데이터베이스에서 JavaScript 표현식을 평가:

`mongo --eval '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JSON.stringify(db.foo.findOne())</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>
