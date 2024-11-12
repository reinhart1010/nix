---
layout: page
title: osx/yabai (한국어)
description: "바이너리 공간 분할을 기반으로 한 macOS 타일링 윈도우 관리자."
content_hash: 68be3cb83cf386de8a727ae7c838c4fdd330f167
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/yabai.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/yabai.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/yabai.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yabai

바이너리 공간 분할을 기반으로 한 macOS 타일링 윈도우 관리자.
더 많은 정보: <https://github.com/koekeishiya/yabai/wiki>.

- 레이아웃 설정을 위한 설정 [m]메시지 전송:

`yabai -m config layout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bsp|stack|float</span>

- 윈도우 간격을 포인트 단위로 설정:

`yabai -m config window_gap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 불투명도 활성화:

`yabai -m config window_opacity on`

- 윈도우 그림자 비활성화:

`yabai -m config window_shadow off`

- 상태 바 활성화:

`yabai -m config status_bar on`
