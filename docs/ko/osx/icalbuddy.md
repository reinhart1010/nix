---
layout: page
title: osx/icalbuddy (한국어)
description: "macOS 캘린더 데이터베이스에서 이벤트와 작업을 출력하는 명령줄 유틸리티."
content_hash: e698dfa6b0c0c3751382faee2f0144c4185c4c0e
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/icalbuddy.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/icalbuddy.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/icalbuddy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# icalBuddy

macOS 캘린더 데이터베이스에서 이벤트와 작업을 출력하는 명령줄 유틸리티.
더 많은 정보: <https://hasseg.org/icalBuddy/>.

- 오늘 나중에 있을 이벤트 표시:

`icalBuddy --includeOnlyEventsFromNowOn eventsToday`

- 완료되지 않은 작업 표시:

`icalBuddy uncompletedTasks`

- 오늘 모든 이벤트를 캘린더별로 구분하여 서식화된 목록으로 표시:

`icalBuddy --formatOutput --separateByCalendar eventsToday`

- 지정된 일수 동안의 작업 표시:

`icalBuddy --includeOnlyEventsFromNowOn "tasksDueBefore:today+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">일_수</span>`"`

- 특정 기간 내의 이벤트 표시:

`icalBuddy eventsFrom:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작_날짜</span>` to:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종료_날짜</span>
