---
layout: page
title: linux/wpa_cli (한국어)
description: "wlan 인터페이스를 추가하고 구성."
content_hash: e244ec2aa429cbd468f38ef96f18d84f493ba13b
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/wpa_cli.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/wpa_cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wpa_cli

wlan 인터페이스를 추가하고 구성.
더 많은 정보: <https://manned.org/wpa_cli>.

- 사용 가능한 네트워크 스캔:

`wpa_cli scan`

- 스캔 결과 표시:

`wpa_cli scan_results`

- 네트워크 추가:

`wpa_cli add_network `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호</span>

- 네트워크의 SSID 설정:

`wpa_cli set_network `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호</span>` ssid "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SSID</span>`"`

- 네트워크 활성화:

`wpa_cli enable_network `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호</span>

- 구성 저장:

`wpa_cli save_config`
