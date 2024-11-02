---
layout: page
title: common/pueue-stash (한국어)
description: "작업을 자동으로 시작하지 않도록 임시 저장."
content_hash: 1ec80c3b44f2d39df081eb3bf812a4768e5bdee6
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pueue-stash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pueue stash

작업을 자동으로 시작하지 않도록 임시 저장.
같이 보기: `pueue start` 및 `pueue enqueue`.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 대기열에 있는 작업 임시 저장:

`pueue stash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 여러 작업을 한 번에 임시 저장:

`pueue stash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 임시 저장된 작업을 즉시 시작:

`pueue start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 선행 작업이 완료되면 실행하도록 작업 대기열에 추가:

`pueue enqueue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>
