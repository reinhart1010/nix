---
layout: page
title: linux/maim (한국어)
description: "스크린샷 유틸리티."
content_hash: 3fd8b3d7374ffadda6b55ff5b009420566766cea
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/maim.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/maim.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># maim

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
