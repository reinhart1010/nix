---
layout: page
title: linux/ip-route-get (한국어)
description: "목적지로 가는 단일 경로를 가져와 커널이 인식하는 그대로 내용을 출력합니다."
content_hash: ef1fcac4f4423e10e82921786cd83b0016dcdcee
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ip-route-get.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ip-route-get.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ip route get

목적지로 가는 단일 경로를 가져와 커널이 인식하는 그대로 내용을 출력합니다.
더 많은 정보: <https://manned.org/ip-route>.

- 목적지로 가는 경로 출력:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>

- 특정 소스 주소에서 목적지로 가는 경로 출력:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스</span>

- 특정 인터페이스를 통해 도착하는 패킷의 목적지로 가는 경로 출력:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지</span>` iif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 특정 인터페이스를 통해 강제로 출력하는 목적지로 가는 경로 출력:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지</span>` oif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>

- 지정된 서비스 유형(ToS)으로 목적지로 가는 경로 출력:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지</span>` tos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0x10</span>

- 특정 VRF(가상 라우팅 및 전달) 인스턴스를 사용하여 목적지로 가는 경로 출력:

`ip route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지</span>` vrf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myvrf</span>
