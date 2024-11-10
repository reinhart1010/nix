---
layout: page
title: linux/openvpn3 (한국어)
description: "OpenVPN 3 Linux 클라이언트."
content_hash: 58a5bd1087d95cb8013b381398d4ffd76bdc3599
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/openvpn3.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/openvpn3.html
    icon: bi bi-globe
tldri18n_status: 2
---
# openvpn3

OpenVPN 3 Linux 클라이언트.
더 많은 정보: <https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux>.

- 새 VPN 세션 시작:

`openvpn3 session-start --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.conf</span>

- 설정된 세션 나열:

`openvpn3 sessions-list`

- 주어진 구성으로 시작된 현재 설정된 세션 연결 해제:

`openvpn3 session-manage --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.conf</span>` --disconnect`

- VPN 구성 가져오기:

`openvpn3 config-import --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.conf</span>

- 가져온 구성 나열:

`openvpn3 configs-list`
