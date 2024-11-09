---
layout: page
title: linux/ip-route-show (한국어)
description: "IP 라우팅 테이블 관리용 하위 명령어."
content_hash: dadc7ff903fec86a66a73fbb48a6b48ce21982c9
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ip-route-show.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip-route-show.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/ip-route-show.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ip-route-show.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ip-route-show.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ip route show

IP 라우팅 테이블 관리용 하위 명령어.
더 많은 정보: <https://manned.org/ip-route>.

- 라우팅 테이블 표시:

`ip route show`

- 메인 라우팅 테이블 표시 (첫 번째 예시와 동일):

`ip route show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main|254</span>

- 로컬 라우팅 테이블 표시:

`ip route show table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local|255</span>

- 모든 라우팅 테이블 표시:

`ip route show table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all|unspec|0</span>

- 특정 장치에서만 경로 나열:

`ip route show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 특정 범위 내의 경로 나열:

`ip route show scope link`

- 라우팅 캐시 표시:

`ip route show cache`

- IPv6 또는 IPv4 경로만 표시:

`ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-6|-4</span>` route show`
