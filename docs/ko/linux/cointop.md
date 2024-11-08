---
layout: page
title: linux/cointop (한국어)
description: "터미널에서 암호화폐를 추적하고 모니터링."
content_hash: a5d3402b2105e100a6aff8210c2512ac9837211c
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/cointop.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cointop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cointop

터미널에서 암호화폐를 추적하고 모니터링.
더 많은 정보: <https://github.com/cointop-sh/cointop>.

- TUI 열기:

`cointop`

- 캐시 지우기:

`cointop clean`

- 현재 보유량을 읽기 쉽게 표시:

`cointop holdings --human`

- 코인의 가격 확인:

`cointop price --coins `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코인_이름1,코인_이름2,...</span>

- 버전 표시:

`cointop version`
