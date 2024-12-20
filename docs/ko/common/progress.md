---
layout: page
title: common/progress (한국어)
description: "실행 중인 coreutils의 진행 상태를 표시/모니터링."
content_hash: ce88479d1be56279af56a114603e68b8867e16f7
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/progress.html
    icon: bi bi-globe
tldri18n_status: 2
---
# progress

실행 중인 coreutils의 진행 상태를 표시/모니터링.
더 많은 정보: <https://github.com/Xfennec/progress>.

- 실행 중인 coreutils의 진행 상태 표시:

`progress`

- 조용한 모드로 실행 중인 coreutils의 진행 상태 표시:

`progress -q`

- 단일 장기 실행 명령을 시작하고 모니터링:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` & progress --monitor --pid $!`

- 완료까지 남은 시간 추정 포함:

`progress --wait --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>
