---
layout: page
title: linux/setxkbmap (한국어)
description: "X Keyboard Extension을 사용하여 키보드를 설정합니다."
content_hash: c0b1ed6728dfd8f832bce65b08cc35230efeab3b
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/setxkbmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# setxkbmap

X Keyboard Extension을 사용하여 키보드를 설정합니다.
더 많은 정보: <https://manned.org/setxkbmap>.

- 키보드를 프랑스어 AZERTY로 설정:

`setxkbmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fr</span>

- 여러 키보드 레이아웃, 변형 및 전환 옵션 설정:

`setxkbmap -layout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us,de</span>` -variant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,qwerty</span>` -option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'grp:alt_caps_toggle'</span>

- 도움말 보기:

`setxkbmap -help`

- 모든 레이아웃 나열:

`localectl list-x11-keymap-layouts`

- 레이아웃의 변형 나열:

`localectl list-x11-keymap-variants `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">de</span>

- 사용 가능한 전환 옵션 나열:

`localectl list-x11-keymap-options | grep grp:`
