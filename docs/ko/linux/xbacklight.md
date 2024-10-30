---
layout: page
title: linux/xbacklight (한국어)
description: "RandR 확장을 사용하여 화면 밝기를 조절하는 유틸리티."
content_hash: a447a369d9a8ada75e1ecb4ae998e0856485a459
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/xbacklight.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/xbacklight.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xbacklight

RandR 확장을 사용하여 화면 밝기를 조절하는 유틸리티.
더 많은 정보: <https://gitlab.freedesktop.org/xorg/app/xbacklight>.

- 현재 화면 밝기를 퍼센트로 확인:

`xbacklight`

- 화면 밝기를 40%로 설정:

`xbacklight -set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40</span>

- 현재 밝기를 25% 증가:

`xbacklight -inc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>

- 현재 밝기를 75% 감소:

`xbacklight -dec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">75</span>

- 60초(밀리초 단위) 동안 60단계로 화면 밝기를 100%로 증가:

`xbacklight -set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` -time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60000</span>` -steps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>
