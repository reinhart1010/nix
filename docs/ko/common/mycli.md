---
layout: page
title: common/mycli (한국어)
description: "자동 완성 및 구문 강조 기능을 제공하는 MySQL 명령줄 클라이언트."
content_hash: c6f50c5992fdae8af4530e3c7c49d8592c890982
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mycli.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/mycli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mycli

자동 완성 및 구문 강조 기능을 제공하는 MySQL 명령줄 클라이언트.
더 많은 정보: <https://mycli.net>.

- 현재 사용자의 사용자명을 사용하여 포트 3306의 로컬 데이터베이스에 연결:

`mycli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 데이터베이스에 연결 (사용자에게 비밀번호 입력이 요청됨):

`mycli -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 다른 호스트의 데이터베이스에 연결:

`mycli -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_호스트</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>
