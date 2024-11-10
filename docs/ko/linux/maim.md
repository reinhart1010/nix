---
layout: page
title: linux/maim (한국어)
description: "스크린샷 유틸리티."
content_hash: 3fd8b3d7374ffadda6b55ff5b009420566766cea
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/maim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# maim

스크린샷 유틸리티.
더 많은 정보: <https://github.com/naelstrof/maim>.

- 스크린샷을 캡처하여 지정된 경로에 저장:

`maim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크린샷.png</span>

- 선택한 영역의 스크린샷 캡처:

`maim --select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크린샷.png</span>

- 선택한 영역의 스크린샷을 캡처하여 클립보드에 저장 (`xclip` 필요):

`maim --select | xclip -selection clipboard -target image/png`

- 현재 활성 창의 스크린샷 캡처 (`xdotool` 필요):

`maim --window $(xdotool getactivewindow) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크린샷.png</span>
