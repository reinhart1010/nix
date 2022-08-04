---
layout: page
title: common/csvgrep (한국어)
description: "csvkit에 포함된 CSV행의 문자열 및 패턴 매칭 필터링."
content_hash: d9aac5d23752e6d9d6fcb881c4133718e8e7f8ff
related_topics:
  - title: English version
    url: /en/common/csvgrep.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/csvgrep.html
    icon: bi bi-globe
---
# csvgrep

csvkit에 포함된 CSV행의 문자열 및 패턴 매칭 필터링.
더 많은 정보: <https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html>.

- 1 열에 특정 문자열이 있는 행 찾기:

`csvgrep -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">찾을_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- 3열 또는 4열에서 특정 정규식 패턴과 일치하는 행 찾기:

`csvgrep -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3,4</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규식_패턴</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>

- "이름" 열에서 "John Doe"가 포함되지 않는 행 찾기:

`csvgrep -i -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">John Doe</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.csv</span>
