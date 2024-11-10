---
layout: page
title: linux/ip (한국어)
description: "라우팅, 디바이스, 정책 라우팅 및 터널을 표시/조작."
content_hash: 74f8cbfcec0363c36686774c38cdf13d219faa64
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/linux/ip.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/ip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ip.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip

라우팅, 디바이스, 정책 라우팅 및 터널을 표시/조작.
`address`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://www.manned.org/ip.8>.

- 인터페이스를 자세한 정보와 함께 나열:

`ip address`

- 네트워크 계층 정보 요약과 함께 인터페이스 나열:

`ip -brief address`

- 링크 계층 정보 요약과 함께 인터페이스 나열:

`ip -brief link`

- 라우팅 테이블 표시:

`ip route`

- 이웃(ARP 테이블) 표시:

`ip neighbour`

- 인터페이스를 활성화/비활성화:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">up|down</span>

- 인터페이스에 IP 주소 추가/삭제:

`ip addr add/del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마스크</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 기본 경로 추가:

`ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>
