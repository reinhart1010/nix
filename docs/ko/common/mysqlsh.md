---
layout: page
title: common/mysqlsh (한국어)
description: "SQL, JavaScript, Python을 지원하는 MySQL의 고급 명령줄 클라이언트."
content_hash: 553c17bea85110c80f11f524fcbc7de20a1931cd
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/mysqlsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mysqlsh

SQL, JavaScript, Python을 지원하는 MySQL의 고급 명령줄 클라이언트.
InnoDB 클러스터 및 문서 저장소 컬렉션 관리를 위한 기능 제공.
더 많은 정보: <https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-commands.html>.

- 대화형 모드로 MySQL Shell 시작:

`mysqlsh`

- MySQL 서버에 연결:

`mysqlsh --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_명</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 서버에서 SQL 문을 실행하고 종료:

`mysqlsh --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --execute '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sql_문</span>`'`

- JavaScript 모드로 MySQL Shell 시작:

`mysqlsh --js`

- Python 모드로 MySQL Shell 시작:

`mysqlsh --py`

- JSON 문서를 MySQL 컬렉션에 가져오기:

`mysqlsh --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>` --schema `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스키마_명</span>` --collection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컬렉션_명</span>

- 상세 출력 활성화:

`mysqlsh --verbose`
