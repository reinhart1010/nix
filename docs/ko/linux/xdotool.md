---
layout: page
title: linux/xdotool (한국어)
description: "X11을 위한 명령줄 자동화 도구."
content_hash: 4f642bace9f19e7e6a811f1165a9d2bc1621c959
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/xdotool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xdotool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xdotool

X11을 위한 명령줄 자동화 도구.
더 많은 정보: <https://manned.org/xdotool>.

- 실행 중인 Firefox 창의 X-Windows 창 ID 검색:

`xdotool search --onlyvisible --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- 오른쪽 마우스 버튼 클릭:

`xdotool click `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- 현재 활성 창의 ID 가져오기:

`xdotool getactivewindow`

- ID가 12345인 창에 포커스 맞추기:

`xdotool windowfocus --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12345</span>

- 각 글자마다 500ms 지연을 두고 메시지 입력:

`xdotool type --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` "Hello world"`

- Enter 키 누르기:

`xdotool key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">KP_Enter</span>
