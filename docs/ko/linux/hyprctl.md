---
layout: page
title: linux/hyprctl (한국어)
description: "Hyprland Wayland 컴포지터의 일부를 제어."
content_hash: 73e812eec22c6125d3c7a2d033b665bd5ec99fe2
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/hyprctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/hyprctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/hyprctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hyprctl

Hyprland Wayland 컴포지터의 일부를 제어.
더 많은 정보: <https://wiki.hyprland.org/Configuring/Using-hyprctl>.

- Hyprland 구성 파일 다시 로드:

`hyprctl reload`

- 활성 창 이름 반환:

`hyprctl activewindow`

- 연결된 입력 장치 모두 나열:

`hyprctl devices`

- 각 속성을 포함한 모든 출력 나열:

`hyprctl workspaces`

- 인수를 사용하여 디스패처 호출:

`hyprctl dispatch exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱</span>

- 구성 키워드를 동적으로 설정:

`hyprctl keyword `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 버전 표시:

`hyprctl version`
