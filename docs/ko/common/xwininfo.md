---
layout: page
title: common/xwininfo (한국어)
description: "창에 대한 정보를 표시."
content_hash: 7ec870326bda8f10304c1fea551ac78b7e95f493
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xwininfo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/xwininfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xwininfo

창에 대한 정보를 표시.
같이 보기: `xprop`, `xkill`.
더 많은 정보: <https://www.x.org/releases/current/doc/man/man1/xwininfo.1.xhtml>.

- 커서를 표시하여 창을 선택하고 해당 속성(아이디, 이름, 크기, 위치 등) 표시:

`xwininfo`

- 모든 창의 트리 구조 표시:

`xwininfo -tree -root`

- 특정 ID를 가진 창의 속성 표시:

`xwininfo -id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이디</span>

- 특정 이름을 가진 창의 속성 표시:

`xwininfo -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 이름으로 검색하여 창의 ID 표시:

`xwininfo -tree -root | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>` | head -1 | perl -ne 'print $1 if /(0x[\da-f]+)/ig;'`
