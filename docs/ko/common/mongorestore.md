---
layout: page
title: common/mongorestore (한국어)
description: "컬렉션이나 데이터베이스를 바이너리 덤프에서 MongoDB 인스턴스로 가져오기 위한 유틸리티."
content_hash: 87633662099950a22384b339c180d94662e7af3d
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/mongorestore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mongorestore

컬렉션이나 데이터베이스를 바이너리 덤프에서 MongoDB 인스턴스로 가져오기 위한 유틸리티.
더 많은 정보: <https://docs.mongodb.com/database-tools/mongorestore/>.

- BSON 데이터 덤프를 디렉토리에서 MongoDB 데이터베이스로 가져오기:

`mongorestore --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 사용자인증을 통해, 특정 포트에서 실행 중인 MongoDB 서버 호스트의 지정된 데이터베이스로 디렉토리의 BSON 데이터 덤프 가져오기 (사용자는 비밀번호를 묻게 됩니다):

`mongorestore --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_호스트:포트</span>` --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --password`

- BSON 파일에서 MongoDB 데이터베이스로 컬렉션 가져오기:

`mongorestore --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 사용자인증을 통해, 특정 포트에서 실행 중인 MongoDB 서버 호스트의 지정된 데이터베이스로 BSON 파일에서 컬렉션 가져오기 (사용자는 비밀번호를 묻게 됩니다):

`mongorestore --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_호스트:포트</span>` --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --password`
