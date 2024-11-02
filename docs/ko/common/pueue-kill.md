---
layout: page
title: common/pueue-kill (한국어)
description: "실행 중인 작업이나 전체 그룹을 종료."
content_hash: d7f92a6d6bf6dd7b0eb18f9b0a3fe2d9e783757e
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pueue-kill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pueue kill

실행 중인 작업이나 전체 그룹을 종료.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 기본 그룹의 모든 작업 종료:

`pueue kill`

- 특정 작업 종료:

`pueue kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 작업과 해당 자식 프로세스 모두 종료:

`pueue kill --children `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 그룹의 모든 작업 종료 및 그룹 일시 중지:

`pueue kill --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>

- 모든 그룹의 모든 작업 종료 및 모든 그룹 일시 중지:

`pueue kill --all`
