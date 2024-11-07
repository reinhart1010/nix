---
layout: page
title: common/pixi-global (한국어)
description: "전역 패키지를 관리."
content_hash: 7dc7773a891df165d05522f568e963ff3c8744fe
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pixi-global.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pixi-global.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pixi global

전역 패키지를 관리.
더 많은 정보: <https://pixi.sh/latest/reference/cli/#global>.

- 패키지를 전역으로 설치하고 경로에 추가:

`pixi global install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 패키지를 전역에서 제거:

`pixi global remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 전역으로 설치된 모든 패키지 나열:

`pixi global list`

- 전역으로 설치된 패키지 업데이트:

`pixi global upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 전역으로 설치된 모든 패키지 업데이트:

`pixi global upgrade-all`
