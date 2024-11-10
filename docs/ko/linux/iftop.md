---
layout: page
title: linux/iftop (한국어)
description: "호스트별 인터페이스의 대역폭 사용량 표시."
content_hash: 609abf910210780a8f8170610bdce3cfe4e41b2f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/iftop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iftop

호스트별 인터페이스의 대역폭 사용량 표시.
더 많은 정보: <https://manned.org/iftop>.

- 대역폭 사용량 표시:

`sudo iftop`

- 지정된 인터페이스의 대역폭 사용량 표시:

`sudo iftop -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 포트 정보를 포함하여 대역폭 사용량 표시:

`sudo iftop -P`

- 트래픽의 막대 그래프를 표시하지 않음:

`sudo iftop -b`

- 호스트명을 조회하지 않음:

`sudo iftop -n`

- 도움말 표시:

`?`
