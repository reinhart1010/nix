---
layout: page
title: common/q (한국어)
description: "CSV 및 TSV 파일에서 SQL 유사 쿼리 실행."
content_hash: 42312860f0e73b44496c4c5f762afaf3fb59e3b5
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/q.html
    icon: bi bi-globe
tldri18n_status: 2
---
# q

CSV 및 TSV 파일에서 SQL 유사 쿼리 실행.
더 많은 정보: <https://harelba.github.io/q>.

- 구분 기호를 ','로 지정하여 CSV 파일 쿼리:

`q -d',' "SELECT * from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`"`

- TSV 파일 쿼리:

`q -t "SELECT * from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`"`

- 헤더 행이 있는 파일 쿼리:

`q -d`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구분자</span>` -H "SELECT * from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`"`

- `stdin`에서 데이터 읽기; 쿼리에서 '-'는 `stdin`의 데이터를 나타냄:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력</span>` | q "select * from -"`

- 두 파일을 공통 열 `c1`을 기준으로 조인 (`f1`과 `f2`로 별칭):

`q "SELECT * FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` f1 JOIN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/다른_파일</span>` f2 ON (f1.c1 = f2.c1)"`

- 출력 구분자와 출력 헤더 행을 사용하여 출력 형식 지정 (참고: 명령은 입력 파일 헤더 또는 쿼리에서 재정의된 열 별칭에 기반하여 열 이름 출력):

`q -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구분자</span>` -O "SELECT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열</span>` as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`"`
