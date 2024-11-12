---
layout: page
title: osx/networksetup (한국어)
description: "네트워크 시스템 환경설정 구성 도구."
content_hash: d35f5a7945066fce997a09fa165da92873cc96bd
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/networksetup.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/networksetup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# networksetup

네트워크 시스템 환경설정 구성 도구.
더 많은 정보: <https://support.apple.com/guide/remote-desktop/about-networksetup-apdd0c5a2d5/mac>.

- 사용 가능한 네트워크 서비스 제공자 나열 (이더넷, Wi-Fi, 블루투스 등):

`networksetup -listallnetworkservices`

- 특정 네트워크 장치의 네트워크 설정 표시:

`networksetup -getinfo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Wi-Fi</span>`"`

- 현재 연결된 Wi-Fi 네트워크 이름 가져오기 (Wi-Fi 장치는 보통 en0 또는 en1):

`networksetup -getairportnetwork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en0</span>

- 특정 Wi-Fi 네트워크에 연결:

`networksetup -setairportnetwork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">무선 네트워크 SSID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>
