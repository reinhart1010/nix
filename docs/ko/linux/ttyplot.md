---
layout: page
title: linux/ttyplot (한국어)
description: "실시간 커맨드라인 플로팅 유틸리티로, `stdin`으로 데이터 입력을 받습니다."
content_hash: 14620b49cf8bd6da985905980c25177446e07cd6
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/ttyplot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ttyplot

실시간 커맨드라인 플로팅 유틸리티로, `stdin`으로 데이터 입력을 받습니다.
더 많은 정보: <https://github.com/tenox7/ttyplot>.

- 값 `1`, `2`, `3`을 플로팅 (`cat`은 ttyplot의 종료를 방지):

`{ echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1 2 3</span>`; cat } | ttyplot`

- 특정 제목과 단위를 설정:

`{ echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1 2 3</span>`; cat } | ttyplot -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단위</span>

- while 루프를 사용하여 랜덤 값을 지속적으로 플로팅:

`{ while `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>`; do echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$RANDOM</span>`; sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`; done } | ttyplot`

- `ping`의 출력을 파싱하여 시각화:

`ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` | sed -u '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s/^.*time=//g; s/ ms//g</span>`' | ttyplot -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8로의 핑</span>`" -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ms</span>
