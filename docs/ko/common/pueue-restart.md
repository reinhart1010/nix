---
layout: page
title: common/pueue-restart (한국어)
description: "작업을 다시 시작."
content_hash: 566edd4fc37e7dc326a18f76f200bad5687c9f65
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pueue-restart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pueue restart

작업을 다시 시작.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 특정 작업 다시 시작:

`pueue restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 여러 작업을 한 번에 다시 시작하고 즉시 시작 (대기열에 넣지 않음):

`pueue restart --start-immediately `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 다른 경로에서 특정 작업 다시 시작:

`pueue restart --edit-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 다시 시작하기 전에 명령 편집:

`pueue restart --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 작업을 제자리에서 다시 시작 (별도의 작업으로 대기열에 넣지 않음):

`pueue restart --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 실패한 모든 작업 다시 시작 및 저장:

`pueue restart --all-failed --stashed`
