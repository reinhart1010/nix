---
layout: page
title: common/mongosh (한국어)
description: "MongoDB의 새로운 쉘로, `mongo`의 대체품입니다."
content_hash: cb1f9cf50f66c215c0317afbacada994fbe8f892
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/mongosh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mongosh

MongoDB의 새로운 쉘로, `mongo`의 대체품입니다.
참고: 모든 연결 옵션은 하나의 문자열로 대체할 수 있습니다: `mongodb://user@host:port/db_name?authSource=authdb_name`.
더 많은 정보: <https://www.mongodb.com/docs/mongodb-shell>.

- 기본 포트(`mongodb://localhost:27017`)를 사용하여 로컬 데이터베이스에 연결:

`mongosh`

- 데이터베이스에 연결:

`mongosh --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 지정된 데이터베이스에서 지정된 사용자 명으로 인증 (비밀번호 입력이 요구됩니다):

`mongosh --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --authenticationDatabase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인증_데이터베이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 데이터베이스에서 JavaScript 표현식을 평가:

`mongosh --eval '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JSON.stringify(db.foo.findOne())</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>
