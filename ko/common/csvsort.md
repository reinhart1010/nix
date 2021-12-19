---
layout: page
title: common/csvsort (한국어)
description: "csvkit에 포함된 CSV 파일을 정렬."
content_hash: 4a37e2e2f16add9dccf0df4a3a238775eec091af
related_topics:
  - title: English version
    url: /en/common/csvsort.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/csvsort.html
    icon: bi bi-globe
---
# csvsort

csvkit에 포함된 CSV 파일을 정렬.
더 많은 정보: <https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html>.

- CSV 파일을 9열을 기준으로 정렬:

`csvsort -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- CSV 파일을 "이름" 열에 따라 내림차순으로 정렬:

`csvsort -r -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- CSV 파일을 2열, 4열을 기준으로 정렬:

`csvsort -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- 데이터 형식과 관계 없이 CSV 파일 정렬:

`csvsort --no-inference -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>
