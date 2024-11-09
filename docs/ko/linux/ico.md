---
layout: page
title: linux/ico (한국어)
description: "다면체 애니메이션을 표시합니다."
content_hash: 8e4d912232837214fb76eec779d60813097f9edb
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ico.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ico.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ico

다면체 애니메이션을 표시합니다.
더 많은 정보: <https://manned.org/ico.1>.

- 0.1초마다 위치가 변경되는 정이십면체의 와이어프레임 표시:

`ico -sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>

- 빨간 면과 파란 배경의 실체 정이십면체 표시:

`ico -faces -noedges -colors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>` -bg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>

- 크기 100x100의 큐브 와이어프레임을 프레임마다 +1+2씩 이동하며 표시:

`ico -obj `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큐브</span>` -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100x100</span>` -delta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+1+2</span>

- 5개의 스레드를 사용하여 선 너비 10의 반전된 정이십면체 와이어프레임 표시:

`ico -i -lw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` -threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
