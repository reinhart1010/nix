---
layout: page
title: common/xkill (한국어)
description: "그래픽 세션에서 창을 대화식으로 종료."
content_hash: 58499b272f18d15d6dc97b5ab037d536862ab20f
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xkill.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/xkill.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/xkill.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/xkill.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/xkill.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/xkill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xkill

그래픽 세션에서 창을 대화식으로 종료.
같이 보기: `kill`, `killall`.
더 많은 정보: <https://www.x.org/releases/current/doc/man/man1/xkill.1.xhtml>.

- 왼쪽 마우스 버튼을 눌러 창을 종료할 수 있는 커서 표시 (다른 마우스 버튼을 눌러 취소):

`xkill`

- 마우스 버튼을 눌러 종료할 창을 선택할 수 있는 커서 표시:

`xkill -button any`

- 특정 ID를 가진 창 종료 (`xwininfo`를 사용하여 창 정보를 얻을 수 있음):

`xkill -id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>
