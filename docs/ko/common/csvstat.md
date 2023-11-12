---
layout: page
title: common/csvstat (한국어)
description: "csvkit에 포함된 CSV 파일의 모든 열에 대한 설명 통계 출력."
content_hash: 8db25135c2f7d8a40c8d7eff89f3421faa8e5d11
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/csvstat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/csvstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csvstat

csvkit에 포함된 CSV 파일의 모든 열에 대한 설명 통계 출력.
더 많은 정보: <https://csvkit.readthedocs.io/en/latest/scripts/csvstat.html>.

- 모든 열에 대한 정보 출력:

`csvstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- 2열 , 4열의 모든 정보 출력:

`csvstat -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- 모든 열의 합계 출력:

`csvstat --sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- 3열에 대한 최대값 길이 출력:

`csvstat -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` --len `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- "이름" 열에 고유 값의 수 출력:

`csvstat -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --unique `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>
