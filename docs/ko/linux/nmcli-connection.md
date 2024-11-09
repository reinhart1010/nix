---
layout: page
title: linux/nmcli-connection (한국어)
description: "NetworkManager와 함께 연결 관리."
content_hash: b901fab6dfe2a4a68a2bb1a124846898537cbf47
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/nmcli-connection.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmcli-connection.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/nmcli-connection.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nmcli-connection.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nmcli connection

NetworkManager와 함께 연결 관리.
이 하위 명령은 `nmcli c`로도 호출할 수 있습니다.
더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- 모든 NetworkManager 연결 나열(이름, UUID, 유형 및 장치 표시):

`nmcli connection`

- 연결 활성화:

`nmcli connection up uuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>

- 연결 비활성화:

`nmcli connection down uuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>

- 자동 구성된 듀얼 스택 연결 생성:

`nmcli connection add ifname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_이름</span>` type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이더넷</span>` ipv4.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto</span>` ipv6.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto</span>

- 고정 IPv6 전용 연결 생성:

`nmcli connection add ifname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_이름</span>` type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이더넷</span>` ip6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::2/64</span>` gw6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::1</span>` ipv6.dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::1</span>` ipv4.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ignore</span>

- 고정 IPv4 전용 연결 생성:

`nmcli connection add ifname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_이름</span>` type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이더넷</span>` ip4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.7/8</span>` gw4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.1</span>` ipv4.dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.1</span>` ipv6.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ignore</span>

- OVPN 파일에서 OpenVPN을 사용하여 VPN 연결 생성:

`nmcli connection import type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">openvpn</span>` file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/vpn_구성.ovpn</span>
