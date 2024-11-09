---
layout: page
title: linux/wofi (한국어)
description: "wlroots 기반 Wayland 컴포지터를 위한 애플리케이션 실행기로, `rofi` 및 `dmenu`와 유사합니다."
content_hash: b4a73024e825308099cff29e805558751df81f82
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/wofi.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/wofi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/wofi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wofi

wlroots 기반 Wayland 컴포지터를 위한 애플리케이션 실행기로, `rofi` 및 `dmenu`와 유사합니다.
더 많은 정보: <https://hg.sr.ht/~scoopta/wofi>.

- 앱 목록 표시:

`wofi --show drun`

- 모든 명령 목록 표시:

`wofi --show run`

- 항목 목록을 `stdin`으로 전달하고 선택한 항목을 `stdout`으로 출력:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">선택1\n선택2\n선택3</span>`" | wofi --dmenu`
