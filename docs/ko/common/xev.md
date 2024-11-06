---
layout: page
title: common/xev (한국어)
description: "X 이벤트의 내용을 출력."
content_hash: 58afb7a050d3a4816c2c45b0ee18dace2368d95a
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xev.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xev

X 이벤트의 내용을 출력.
더 많은 정보: <https://gitlab.freedesktop.org/xorg/app/xev>.

- 발생하는 모든 X 이벤트 모니터링:

`xev`

- 새 창을 생성하지 않고 루트 창의 모든 X 이벤트 모니터링:

`xev -root`

- 특정 창의 모든 X 이벤트 모니터링:

`xev -id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">창_ID</span>

- 주어진 카테고리의 X 이벤트 모니터링 (여러 번 지정 가능):

`xev -event `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이벤트_카테고리</span>
