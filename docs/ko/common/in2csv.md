---
layout: page
title: common/in2csv (한국어)
description: "다양한 표 데이터 형식을 CSV로 변환."
content_hash: ce9fc84af8d5e770414e9c45abd08f9c192485ce
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/in2csv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# in2csv

다양한 표 데이터 형식을 CSV로 변환.
csvkit에 포함.
더 많은 정보: <https://csvkit.readthedocs.io/en/latest/scripts/in2csv.html>.

- XLS 파일을 CSV로 변환:

`in2csv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.xls</span>

- DBF 파일을 CSV 파일로 변환:

`in2csv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.dbf</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- 특정 시트를 XLSX 파일에서 CSV로 변환:

`in2csv --sheet=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시트_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.xlsx</span>

- JSON 파일을 in2csv로 파이프:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.json</span>` | in2csv -f json > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>
