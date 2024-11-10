---
layout: page
title: linux/rofi (한국어)
description: "애플리케이션 실행기 및 창 전환기."
content_hash: 29e38edde4d34b226e0404036a032f8c3c12e6dd
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rofi.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/rofi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rofi

애플리케이션 실행기 및 창 전환기.
더 많은 정보: <https://github.com/davatorium/rofi>.

- 앱 목록 표시:

`rofi -show drun`

- 모든 명령 목록 표시:

`rofi -show run`

- 창 간 전환:

`rofi -show window`

- 항목 목록을 `stdin`으로 전달하고 선택한 항목을 `stdout`으로 출력:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">선택1\n선택2\n선택3</span>`" | rofi -dmenu`
