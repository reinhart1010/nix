---
layout: page
title: common/pueue-edit (한국어)
description: "저장되거나 대기 중인 작업의 명령어나 경로를 편집."
content_hash: 3a5c4ea721972e72020431849a925c64e173859e
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pueue-edit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pueue edit

저장되거나 대기 중인 작업의 명령어나 경로를 편집.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 작업 편집, 작업 ID를 확인하려면 `pueue status` 사용:

`pueue edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 작업이 실행되는 경로 편집:

`pueue edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>` --path`

- 지정된 편집기로 명령어 편집:

`EDITOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nano</span>` pueue edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>
