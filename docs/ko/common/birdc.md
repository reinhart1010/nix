---
layout: page
title: common/birdc (한국어)
description: "BIRD 원격 제어."
content_hash: 014a74f7854fad9fcd9ad35ad3063e5955c2be53
last_modified_at: 2024-09-21
related_topics:
  - title: Deutsch version
    url: /de/common/birdc.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/birdc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/birdc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># birdc

BIRD 원격 제어.
bird로부터 경로와 같은 정보를 검색하고 런타임 중에 구성을 수행.
더 많은 정보: <https://bird.network.cz/>.

- 원격 제어 콘솔을 열기:

`birdc`

- BIRD를 다시 시작하지 않고 구성을 다시 로드:

`birdc configure`

- BIRD의 현재 상태를 표시:

`birdc show status`

- 구성된 모든 프로토콜 표시:

`birdc show protocols`

- 프로토콜에 대한 모든 세부정보 표시:

`birdc show protocols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">upstream1</span>` all`

- 특정 AS 번호를 포함하는 모든 경로 표시:

`birdc "show route where bgp_path ~ [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4242120045</span>`]"`

- 모든 최적 경로 표시:

`birdc show route primary`

- 특정 접두사에서 모든 경로의 모든 세부 정보를 표시:

`birdc show route for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fd00:/8</span>` all`
