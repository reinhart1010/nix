---
layout: page
title: linux/ip-route (한국어)
description: "IP 라우팅 테이블 관리 하위 명령."
content_hash: 84162e5d3b2c580f4aebbfa18a75d3c7a2d43c38
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ip-route.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip-route.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ip-route.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ip route

IP 라우팅 테이블 관리 하위 명령.
더 많은 정보: <https://manned.org/ip-route>.

- 라우팅 테이블 표시:

`ip route `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show|list</span>

- 게이트웨이 포워딩을 사용하여 기본 라우트 추가:

`sudo ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게이트웨이_IP</span>

- `eth0`을 사용하여 기본 라우트 추가:

`sudo ip route add default dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 고정 라우트 추가:

`sudo ip route add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_IP</span>` via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게이트웨이_IP</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 고정 라우트 삭제:

`sudo ip route del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_IP</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 고정 라우트 변경 또는 대체:

`sudo ip route `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">change|replace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_IP</span>` via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게이트웨이_IP</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 특정 IP 주소에 도달하기 위해 커널이 사용할 라우트 표시:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_IP</span>
