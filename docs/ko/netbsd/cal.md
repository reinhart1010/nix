---
layout: page
title: netbsd/cal (한국어)
description: "달력을 표시합니다."
content_hash: 613e45779f5b30cb419d66c321d4261c50566b0b
last_modified_at: 2024-09-19
related_topics:
  - title: English version
    url: /en/netbsd/cal.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/cal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cal

달력을 표시합니다.
더 많은 정보: <https://man.netbsd.org/cal.1>.

- 현재 월의 달력 표시:

`cal`

- 특정 연도의 달력 표시:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연도</span>

- 특정 월과 연도의 달력 표시:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">월</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연도</span>

- 1부터 시작하는 율리우스력을 사용해 현재 연도의 전체 달력 표시:

`cal -y -j`

- 오늘을 강조하고 날짜를 포함해 3개월 표시:

`cal -h -3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">월</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연도</span>

- 현재 연도의 특정 월의 이전 2개월과 이후 3개월 표시:

`cal -A 3 -B 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">월</span>

- 지정한 월의 이전 및 이후의 월 수를 지정:

`cal -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">월 수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">월</span>

- 주의 시작 요일을 지정 (0: 일요일, 1: 월요일, ..., 6: 토요일):

`cal -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..6</span>
