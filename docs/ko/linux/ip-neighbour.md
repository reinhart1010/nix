---
layout: page
title: linux/ip-neighbour (한국어)
description: "Neighbour/ARP 테이블 관리 IP 하위 명령어."
content_hash: bb184f356fe0faff0032a3e11525427f4e6eeb26
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/ip-neighbour.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip-neighbour.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip neighbour

Neighbour/ARP 테이블 관리 IP 하위 명령어.
더 많은 정보: <https://manned.org/ip-neighbour.8>.

- Neighbour/ARP 테이블 항목 표시:

`ip neighbour`

- `eth0` 장치에서 neighbour 테이블의 항목 제거:

`sudo ip neighbour flush dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Neighbour 조회를 수행하고 neighbour 항목 반환:

`ip neighbour get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조회_아이피</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Neighbour IP 주소에 대한 ARP 항목을 `eth0`에 추가하거나 삭제:

`sudo ip neighbour `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|del</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피_주소</span>` lladdr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">맥_주소</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` nud reachable`

- Neighbour IP 주소에 대한 ARP 항목을 `eth0`에 변경하거나 대체:

`sudo ip neighbour `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">change|replace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피_주소</span>` lladdr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_맥_주소</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>
