---
layout: page
title: common/mongodump (한국어)
description: "MongoDB 인스턴스의 내용을 내보내는 유틸리티."
content_hash: 26b74291a9cf4599c16b64c9bcaee2821d0db797
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/mongodump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mongodump

MongoDB 인스턴스의 내용을 내보내는 유틸리티.
더 많은 정보: <https://docs.mongodb.com/database-tools/mongodump/>.

- 모든 데이터베이스의 덤프 생성 (파일은 "dump"라는 폴더에 저장됨):

`mongodump`

- 덤프의 출력 위치 지정:

`mongodump --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 데이터베이스의 덤프 생성:

`mongodump --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 특정 데이터베이스 내의 특정 컬렉션 덤프 생성:

`mongodump --collection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컬렉션_이름</span>` --db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 주어진 포트에서 실행 중인 특정 호스트에 연결하여 덤프 생성:

`mongodump --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 특정 사용자 명으로 데이터베이스의 덤프 생성; 사용자에게 비밀번호 입력이 요청됨:

`mongodump --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스</span>` --password`

- 특정 인스턴스에서 덤프 생성; 호스트, 사용자, 비밀번호 및 데이터베이스가 연결 문자열에 정의됨:

`mongodump --uri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연결_문자열</span>
