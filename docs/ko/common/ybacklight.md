---
layout: page
title: common/ybacklight (한국어)
description: "화면 백라이트 밝기 관리. 같이 보기: `xbacklight`."
content_hash: a911df9cbe802b3b8841ce6c9c622a5988ff4782
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/ybacklight.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ybacklight.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ybacklight

화면 백라이트 밝기 관리. 같이 보기: `xbacklight`.
더 많은 정보: <https://github.com/pixelcmtd/ybacklight>.

- 현재 밝기와 최대 밝기를 슬래시로 구분하여 짧게 출력:

`ybacklight Sc/Sm`

- 밝기 지정:

`ybacklight s`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">420</span>

- 밝기를 42 큰 단계(기본값 4200)만큼 증가:

`ybacklight Si42`

- 밝기를 300만큼 감소:

`ybacklight d300`
