---
layout: page
title: common/pueue-follow (한국어)
description: "현재 실행 중인 작업의 출력을 따라가기."
content_hash: a1353e1a85fc990668068a21d07339cc7caa43c4
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pueue-follow.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pueue follow

현재 실행 중인 작업의 출력을 따라가기.
같이 보기: `pueue log`.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 작업의 출력(`stdout` + `stderr`)을 따라가기:

`pueue follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 작업의 `stderr`를 따라가기:

`pueue follow --err `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>
