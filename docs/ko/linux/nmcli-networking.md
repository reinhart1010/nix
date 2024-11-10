---
layout: page
title: linux/nmcli-networking (한국어)
description: "NetworkManager의 네트워킹 상태를 관리합니다."
content_hash: 69c9770b20e71148b70a2c04179e1d8c2dd10f2f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/nmcli-networking.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmcli-networking.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli networking

NetworkManager의 네트워킹 상태를 관리합니다.
이 하위 명령은 `nmcli n`으로도 호출할 수 있습니다.
더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- NetworkManager의 네트워킹 상태 표시:

`nmcli networking`

- NetworkManager가 관리하는 네트워킹 및 모든 인터페이스 활성화 또는 비활성화:

`nmcli networking `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- 마지막으로 알려진 연결 상태 표시:

`nmcli networking connectivity`

- 현재 연결 상태 확인:

`nmcli networking connectivity check`
