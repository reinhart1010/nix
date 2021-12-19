---
layout: page
title: common/csvformat (한국어)
description: "csvkit에 포함된 CSV 파일을 사용자 정의 출력으로 변환."
content_hash: 4e1d50a46bd74c76ab1d9a09cb014fc24c1888bc
related_topics:
  - title: English version
    url: /en/common/csvformat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/csvformat.html
    icon: bi bi-globe
---
# csvformat

csvkit에 포함된 CSV 파일을 사용자 정의 출력으로 변환.
더 많은 정보: <https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html>.

- 탭으로 구분된 파일(TSV)로 변환:

`csvformat -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- 구분자를 사용자 지정 문자로 변환:

`csvformat -D "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_지정_문자</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- 라인의 끝을 캐리지 리턴 (^M) + 라인 바꿈으로 변환:

`csvformat -M "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\r\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- 인용문 사용 최소화:

`csvformat -U 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- 인용문 사용 최대화:

`csvformat -U 1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>
