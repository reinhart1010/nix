---
layout: page
title: common/xprop (한국어)
description: "X 서버에서 창 및 폰트 속성을 표시."
content_hash: 75019e6e6e69849c2aa4d4c555e251bc7d6dcf93
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xprop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xprop

X 서버에서 창 및 폰트 속성을 표시.
더 많은 정보: <https://manned.org/xprop>.

- 루트 창의 이름 표시:

`xprop -root WM_NAME`

- 창의 윈도우 매니저 힌트 표시:

`xprop -name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">창_이름</span>`" WM_HINTS`

- 폰트의 포인트 크기 표시:

`xprop -font "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폰트_이름</span>`" POINT_SIZE`

- ID가 0x200007인 창의 모든 속성 표시:

`xprop -id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0x200007</span>
