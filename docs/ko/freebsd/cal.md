---
layout: page
title: freebsd/cal (한국어)
description: "현재 날짜가 강조된 달력을 표시합니다."
content_hash: 27e1335d0ca21d61747112f5e4b48c6133a4ffdf
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/freebsd/cal.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/cal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cal

현재 날짜가 강조된 달력을 표시합니다.
더 많은 정보: <https://man.freebsd.org/cgi/man.cgi?cal>.

- 현재 월의 달력 표시:

`cal`

- 특정 연도의 달력 표시:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연도</span>

- 특정 월과 연도의 달력 표시:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">월</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연도</span>

- 현재 연도의 전체 달력 표시:

`cal -y`

- 오늘을 강조하지 않고 날짜를 중심으로 [3]개월 표시:

`cal -h -3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">월</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">연도</span>

- 현재 연도의 특정 월의 이전 2개월과 이후 3개월 표시:

`cal -A 3 -B 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">월</span>

- 율리우스력 날짜 표시 (1부터 시작하여 1월 1일부터 번호 매김):

`cal -j`
