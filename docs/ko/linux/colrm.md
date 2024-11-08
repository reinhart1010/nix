---
layout: page
title: linux/colrm (한국어)
description: "`stdin`에서 열을 제거합니다."
content_hash: ee3aef1e3bcbc02d347dc199aa5219132da33718
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/colrm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/colrm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># colrm

`stdin`에서 열을 제거합니다.
더 많은 정보: <https://manned.org/colrm>.

- `stdin`의 첫 번째 열 제거:

`colrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1 1</span>

- 각 줄의 3번째 열부터 끝까지 제거:

`colrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- 각 줄의 3번째 열부터 5번째 열까지 제거:

`colrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3 5</span>
