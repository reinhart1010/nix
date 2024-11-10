---
layout: page
title: common/task (한국어)
description: "명령줄 할 일 목록 관리 도구."
content_hash: e4a7042cac9a652efec70e9cbe33cc1fe7d3ccd1
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/task.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/task.html
    icon: bi bi-globe
tldri18n_status: 2
---
# task

명령줄 할 일 목록 관리 도구.
더 많은 정보: <https://taskwarrior.org/docs/>.

- 내일까지 완료해야 할 새로운 작업 추가:

`task add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설명</span>` due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내일</span>

- 작업의 우선순위 업데이트:

`task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>` modify priority:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">H|M|L</span>

- 작업 완료:

`task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>` done`

- 작업 삭제:

`task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>` delete`

- 모든 열려 있는 작업 나열:

`task list`

- 이번 주 말까지 마감인 열려 있는 작업 나열:

`task list due.before:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주말</span>

- 일별 그래픽 번다운 차트 표시:

`task burndown.daily`

- 모든 보고서 나열:

`task reports`
