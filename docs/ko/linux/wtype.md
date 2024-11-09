---
layout: page
title: linux/wtype (한국어)
description: "Wayland에서 키보드 입력을 시뮬레이트합니다. X11의 `xdotool type`과 유사합니다."
content_hash: 2501ea8a0e75312b301e2a2db856478c75584982
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/wtype.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/wtype.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wtype

Wayland에서 키보드 입력을 시뮬레이트합니다. X11의 `xdotool type`과 유사합니다.
같이 보기: `ydotool`.
더 많은 정보: <https://github.com/atx/wtype>.

- 텍스트 입력을 시뮬레이트:

`wtype "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- 특정 키 입력:

`wtype -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Left</span>

- 수정 키 누르기:

`wtype -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shift|ctrl|...</span>

- 수정 키 놓기:

`wtype -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ctrl</span>

- 키 입력 간 대기 시간 설정 (밀리초):

`wtype -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` -- "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>`"`

- `stdin`에서 텍스트 읽기:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>`" | wtype -`
