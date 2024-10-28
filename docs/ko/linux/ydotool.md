---
layout: page
title: linux/ydotool (한국어)
description: "디스플레이 서버와 무관하게 명령을 통해 키보드 및 마우스 입력을 제어."
content_hash: efdc293857937746fed163388013e97e9cb78b3d
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/linux/ydotool.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ydotool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ydotool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ydotool

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
