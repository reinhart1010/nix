---
layout: page
title: linux/xset (한국어)
description: "X를 위한 사용자 환경 설정 도구."
content_hash: f617709f7fcf6157164ce6d28b909c26b5d54f83
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/xset.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xset

X를 위한 사용자 환경 설정 도구.
더 많은 정보: <https://manned.org/xset>.

- 화면 보호기 비활성화:

`xset s off`

- 벨 소리 비활성화:

`xset b off`

- 비활성 상태 60분 후 화면 보호기 시작 설정:

`xset s 3600 3600`

- DPMS (Energy Star) 기능 비활성화:

`xset -dpms`

- DPMS (Energy Star) 기능 활성화:

`xset +dpms`

- 특정 X 서버의 정보 조회:

`xset -display :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` q`
