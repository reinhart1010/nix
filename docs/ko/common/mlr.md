---
layout: page
title: common/mlr (한국어)
description: "Miller는 CSV, TSV 및 표 형식 JSON과 같은 이름으로 색인된 데이터를 위한 `awk`, `sed`, `cut`, `join`, `sort`와 유사합니다."
content_hash: e075cafca59875cd9715152cbc447fe2079cfca2
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mlr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mlr

Miller는 CSV, TSV 및 표 형식 JSON과 같은 이름으로 색인된 데이터를 위한 `awk`, `sed`, `cut`, `join`, `sort`와 유사합니다.
더 많은 정보: <https://johnkerl.org/miller/doc>.

- CSV 파일을 표 형식으로 보기 좋게 출력:

`mlr --icsv --opprint cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제.csv</span>

- JSON 데이터를 받아 출력 형식을 보기 좋게 출력:

`echo '{"hello":"world"}' | mlr --ijson --opprint cat`

- 특정 필드를 알파벳 순서로 정렬:

`mlr --icsv --opprint sort -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제.csv</span>

- 특정 필드를 내림차순 숫자 순서로 정렬:

`mlr --icsv --opprint sort -nr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제.csv</span>

- CSV를 JSON으로 변환하며 계산 수행 및 계산 결과 표시:

`mlr --icsv --ojson put '$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새필드1</span>` = $`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옛필드A</span>`/$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옛필드B</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제.csv</span>

- JSON을 받아 출력 형식을 수직 JSON으로 포맷:

`echo '{"hello":"world", "foo":"bar"}' | mlr --ijson --ojson --jvstack cat`

- 압축된 CSV 파일의 숫자를 문자열로 처리하여 행 필터링:

`mlr --prepipe 'gunzip' --csv filter -S '$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드명</span>` =~ "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`"' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제.csv.gz</span>
