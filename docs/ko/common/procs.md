---
layout: page
title: common/procs (한국어)
description: "활성 프로세스에 대한 정보를 표시."
content_hash: 1fdfd155e69c6694e4f2d3cbc275697b53481872
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/procs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# procs

활성 프로세스에 대한 정보를 표시.
더 많은 정보: <https://github.com/dalance/procs>.

- PID, 사용자, CPU 사용량, 메모리 사용량 및 시작한 명령을 보여주는 모든 프로세스 나열:

`procs`

- 트리 형태로 모든 프로세스 나열:

`procs --tree`

- 시작한 명령에 Zsh가 포함된 프로세스 정보 나열:

`procs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>

- CPU 시간으로 [a]scending 또는 [d]escending 순서로 정렬된 모든 프로세스 정보 나열:

`procs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--sorta|--sortd</span>` cpu`

- PID, 명령 또는 사용자에 `41` 또는 `firefox`가 포함된 프로세스 정보 나열:

`procs --or `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID|command|user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">41</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- PID `41`과 명령 또는 사용자에 `zsh`가 포함된 프로세스 정보 나열:

`procs --and `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">41</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>
