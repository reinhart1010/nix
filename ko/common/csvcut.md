---
layout: page
title: common/csvcut (한국어)
description: "유닉스의 `cut` 명령어와 같이 CSV 파일 필터링 및 잘라내기, tabular 데이터 보존을 위해. csvkit에 포함된 CSV 파일만 해당."
content_hash: fd47be75ce5f1b85037e6ea87a98bf6b7bb359a0
related_topics:
  - title: English version
    url: /en/common/csvcut.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/csvcut.html
    icon: bi bi-globe
---
# csvcut

유닉스의 `cut` 명령어와 같이 CSV 파일 필터링 및 잘라내기, tabular 데이터 보존을 위해. csvkit에 포함된 CSV 파일만 해당.
더 많은 정보: <https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html>.

- 모든 열의 인덱스 및 이름 출력:

`csvcut -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- 첫번째 및 세번째 열 출력:

`csvcut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- 네번째 열을 **제외한** 모든 열 출력:

`csvcut -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- "id" 및 "first name" (이 순서대로) 열 출력:

`csvcut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id,"first name"</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>
