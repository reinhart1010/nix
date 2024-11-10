---
layout: page
title: linux/nmcli-general (한국어)
description: "NetworkManager의 일반 설정을 관리합니다."
content_hash: 1cf16203dc189bbbd88a5b80ac4a646b3a176787
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/nmcli-general.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmcli-general.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli general

NetworkManager의 일반 설정을 관리합니다.
이 하위 명령은 `nmcli g`로도 호출할 수 있습니다.
더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- NetworkManager의 일반 상태 표시:

`nmcli general`

- 현재 장치의 호스트명 표시:

`nmcli general hostname`

- 현재 장치의 호스트명 변경:

`sudo nmcli general hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_호스트명</span>

- NetworkManager의 권한 표시:

`nmcli general permissions`

- 현재 로깅 수준 및 도메인 표시:

`nmcli general logging`

- 로깅 수준 및/또는 도메인 설정 (`man NetworkManager.conf`에서 사용 가능한 모든 도메인 확인):

`nmcli general logging level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INFO|OFF|ERR|WARN|DEBUG|TRACE</span>` domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_1,도메인_2,...</span>
