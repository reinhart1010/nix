---
layout: page
title: linux/ydotool (한국어)
description: "디스플레이 서버와 무관하게 명령을 통해 키보드 및 마우스 입력을 제어."
content_hash: efdc293857937746fed163388013e97e9cb78b3d
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/ydotool.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ydotool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ydotool

디스플레이 서버와 무관하게 명령을 통해 키보드 및 마우스 입력을 제어.
더 많은 정보: <https://github.com/ReimuNotMoe/ydotool>.

- ydotool 데몬을 백그라운드에서 시작:

`ydotoold`

- 왼쪽 클릭 입력 수행:

`ydotool click 0xC0`

- 오른쪽 클릭 입력 수행:

`ydotool click 0xC1`

- Alt+F4 입력:

`ydotool key 56:1 62:1 62:0 56:0`
