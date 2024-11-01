---
layout: page
title: common/mysql (한국어)
description: "MySQL 명령줄 도구."
content_hash: 24c1912f071e479bd4d54103a5a4f5b0b8d7ef4d
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/mysql.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mysql.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/mysql.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/mysql.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mysql.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/mysql.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mysql

MySQL 명령줄 도구.
더 많은 정보: <https://www.mysql.com/>.

- 데이터베이스에 연결:

`mysql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 데이터베이스에 연결하고, 비밀번호 입력 요청:

`mysql -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 다른 호스트의 데이터베이스에 연결:

`mysql -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_호스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- Unix 소켓을 통해 데이터베이스에 연결:

`mysql --socket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/socket.sock</span>

- 스크립트 파일(배치 파일)에서 SQL 문 실행:

`mysql -e "source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.sql</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- `mysqldump`로 생성된 백업에서 데이터베이스 복원 (비밀번호 입력 요청):

`mysql --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/backup.sql</span>

- 백업에서 모든 데이터베이스 복원 (비밀번호 입력 요청):

`mysql --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` --password < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/backup.sql</span>
