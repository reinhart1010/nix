---
layout: page
title: openbsd/cal (한국어)
description: "현재 날짜가 강조된 달력을 표시합니다."
content_hash: 55ff64a8a846313e9738544ec39a7ed6643a11b2
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/openbsd/cal.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/cal.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/cal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cal

현재 날짜가 강조된 달력을 표시합니다.
더 많은 정보: <https://man.openbsd.org/cal>.

- 현재 월의 달력 표시:

`cal`

- 특정 년도의 달력 표시:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">년도</span>

- 특정 월과 년도의 달력 표시:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">월</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">년도</span>

- 현재 년도의 달력 표시:

`cal -y`

- [j]율리우스력 표시 (1부터 시작되며 1월 1일부터 번호 부여됨):

`cal -j`

- 일요일 대신에 [m]월요일을 주 시작으로 사용:

`cal -m`

- [w]주 번호 표시 (`-j`와 호환되지 않음):

`cal -w`
