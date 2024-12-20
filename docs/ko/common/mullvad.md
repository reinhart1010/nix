---
layout: page
title: common/mullvad (한국어)
description: "Mullvad VPN을 위한 CLI 클라이언트."
content_hash: b97f0098e9b096379f407b4a08f9fb48bd8b5b68
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mullvad.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/mullvad.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mullvad

Mullvad VPN을 위한 CLI 클라이언트.
같이 보기: `fastd`, `ivpn`, `mozillavpn`, `warp-cli`.
더 많은 정보: <https://mullvad.net/>.

- 지정된 계정 번호로 Mullvad 계정 연결:

`mullvad account set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정_번호</span>

- VPN이 켜져 있는 동안 LAN 액세스 허용:

`mullvad lan set allow`

- VPN 터널 연결:

`mullvad connect`

- VPN 터널 상태 확인:

`mullvad status`
