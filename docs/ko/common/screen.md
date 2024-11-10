---
layout: page
title: common/screen (한국어)
description: "원격 서버에서 세션을 열어 유지. 단일 SSH 연결로 여러 창을 관리."
content_hash: 6e9ea021910d43abe9af70ebd71c466d6d2643b5
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/screen.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/screen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# screen

원격 서버에서 세션을 열어 유지. 단일 SSH 연결로 여러 창을 관리.
같이 보기: `tmux`, `zellij`.
더 많은 정보: <https://manned.org/screen>.

- 새 screen 세션 시작:

`screen`

- 새 이름 지정 screen 세션 시작:

`screen -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_이름</span>

- 새로운 데몬을 시작하고 출력을 `screenlog.x`에 기록:

`screen -dmLS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 열린 screen 세션 표시:

`screen -ls`

- 열린 screen에 다시 연결:

`screen -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_이름</span>

- screen 내부에서 분리:

`<Ctrl> + A, D`

- 현재 screen 세션 종료:

`<Ctrl> + A, K`

- 분리된 screen 종료:

`screen -X -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_이름</span>` quit`
