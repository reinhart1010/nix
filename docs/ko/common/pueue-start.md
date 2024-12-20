---
layout: page
title: common/pueue-start (한국어)
description: "작업 또는 작업 그룹의 실행을 재개."
content_hash: b07777896745edb2b5c0f1a39932436a9dac34dc
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pueue-start.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pueue start

작업 또는 작업 그룹의 실행을 재개.
같이 보기: `pueue pause`.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 기본 그룹의 모든 작업 재개:

`pueue start`

- 특정 작업 재개:

`pueue start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 여러 작업을 동시에 재개:

`pueue start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 모든 작업과 그 하위 작업 재개:

`pueue start --all --children`

- 특정 그룹의 모든 작업 재개:

`pueue start group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>
