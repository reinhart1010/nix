---
layout: page
title: common/neo4j-admin (한국어)
description: "Neo4j DBMS(데이터베이스 관리 시스템) 관리 및 운영."
content_hash: 14e13ec5265732252325b678ea54321c5d49e74f
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/neo4j-admin.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/neo4j-admin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# neo4j-admin

Neo4j DBMS(데이터베이스 관리 시스템) 관리 및 운영.
같이 보기: `cypher-shell`, `mysqld`.
더 많은 정보: <https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/>.

- DBMS 시작:

`neo4j-admin server start`

- DBMS 중지:

`neo4j-admin server stop`

- 기본 `neo4j` 사용자의 초기 비밀번호 설정 (DBMS를 처음 시작하기 위한 전제 조건):

`neo4j-admin dbms set-initial-password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 오프라인 데이터베이스의 아카이브(덤프)를 `database_name.dump`라는 이름의 파일로 생성:

`neo4j-admin database dump --to-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- `database_name.dump`라는 아카이브에서 데이터베이스 로드:

`neo4j-admin database load --from-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` --overwrite-destination=true`

- 지정된 아카이브 파일을 `stdin`을 통해 데이터베이스 로드:

`neo4j-admin database load --from-stdin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` --overwrite-destination=true < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름.dump</span>

- 도움말 표시:

`neo4j-admin --help`
