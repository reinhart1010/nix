---
layout: page
title: common/duckdb (한국어)
description: "처리 중인 분석 SQL 엔진인 DuckDB용 명령줄 클라이언트."
content_hash: 4d5798022071ed1122bb83c4d70aa51be50d7f94
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/duckdb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duckdb

처리 중인 분석 SQL 엔진인 DuckDB용 명령줄 클라이언트.
더 많은 정보: <https://duckdb.org>.

- 임시 메모리 내 데이터베이스를 사용하여 대화형 쉘을 시작:

`duckdb`

- 데이터베이스 파일에서 대화형 쉘을 시작. 파일이 없으면, 새로운 데이터베이스가 생성됨:

`duckdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터베이스파일</span>

- CSV, JSON 또는 Parquet 파일을 직접 쿼리:

`duckdb -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SELECT * FROM 'data_source.[csv|csv.gz|json|json.gz|parquet]'</span>`"`

- SQL 스크립트를 실행:

`duckdb -c ".read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sql</span>`"`

- 데이터베이스 파일에 대해 쿼리를 실행하고 대화형 쉘을 열어둠:

`duckdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터베이스파일</span>` -cmd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SELECT DISTINCT * FROM tbl</span>`"`

- 데이터베이스 파일에서 SQL 쿼리를 실행하고 대화형 쉘을 열어둠:

`duckdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터베이스파일</span>` -init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sql</span>

- `stdin`에서 CSV를 읽고 `stdout`에 CSV를 쓰기:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.csv</span>` | duckdb -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">COPY (FROM read_csv('/dev/stdin')) TO '/dev/stdout' WITH (FORMAT CSV, HEADER)</span>`"`

- 도움말 표시:

`duckdb -help`
