---
layout: page
title: linux/slurp (한국어)
description: "Wayland 컴포지터에서 영역을 선택."
content_hash: 569f20dd800e030acab4d1d53cacba5bf537705e
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/slurp.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/slurp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/slurp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># slurp

Wayland 컴포지터에서 영역을 선택.
더 많은 정보: <https://github.com/emersion/slurp>.

- 영역을 선택하고 `stdout`에 출력:

`slurp`

- 영역을 선택하고 선택한 영역의 크기를 표시하면서 `stdout`에 출력:

`slurp -d`

- 영역 대신 단일 지점 선택:

`slurp -p`

- 출력물을 선택하고 그 이름을 출력:

`slurp -o -f '%o'`

- 특정 영역을 선택하고 `grim`을 사용하여 테두리가 없는 스크린샷 찍기:

`grim -g "$(slurp -w 0)"`

- 특정 영역을 선택하고 `wf-recorder`를 사용하여 테두리가 없는 비디오 촬영:

`wf-recorder --geometry "$(slurp -w 0)"`
