---
layout: page
title: linux/pactree (한국어)
description: "pacman용 패키지 의존성 트리 뷰어."
content_hash: b3d0bc8987ee11b79beb113d36f6229907ba9ab0
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pactree.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pactree.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pactree

pacman용 패키지 의존성 트리 뷰어.
더 많은 정보: <https://manned.org/pactree.8>.

- 특정 패키지의 의존성 트리를 출력:

`pactree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 패키지에 의존하는 패키지 출력:

`pactree --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 중복을 생략하고 의존성을 한 줄에 하나씩 출력:

`pactree --unique `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 패키지의 선택적 의존성을 포함하고 출력을 색상으로 표시:

`pactree --optional --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 도움말 표시:

`pactree`
