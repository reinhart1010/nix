---
layout: page
title: linux/blight (한국어)
description: "디스플레이 밝기를 변경하는 유틸리티."
content_hash: 9673fb6de254ff129dbe50b7f52724ba331f3a7d
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/blight.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/blight.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/blight.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># blight

디스플레이 밝기를 변경하는 유틸리티.
더 많은 정보: <https://github.com/gutjuri/blight>.

- 디스플레이 밝기를 50%로 설정:

`blight set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` -r`

- 현재 디스플레이 밝기 표시:

`blight show`

- 최대 디스플레이 밝기 출력:

`blight max`

- 디스플레이 밝기를 %만큼 증가:

`blight inc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` -r`

- 내부 단위로 디스플레이 밝기 감소:

`blight dec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>
