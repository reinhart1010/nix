---
layout: page
title: linux/networkctl (한국어)
description: "네트워크 링크의 상태를 조회합니다."
content_hash: c06cb7dfe25db3d1a7ba07af8a9e98a305563387
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/networkctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/networkctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# networkctl

네트워크 링크의 상태를 조회합니다.
`systemd-networkd`를 사용하여 네트워크 구성을 관리합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/networkctl.html>.

- 기존 링크와 그 상태를 나열:

`networkctl list`

- 전체 네트워크 상태 표시:

`networkctl status`

- 네트워크 장치를 활성화:

`networkctl up `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스1 인터페이스2 ...</span>

- 네트워크 장치를 비활성화:

`networkctl down `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스1 인터페이스2 ...</span>

- 동적 구성 갱신 (예: DHCP 서버로부터 받은 IP 주소):

`networkctl renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스1 인터페이스2 ...</span>

- 구성 파일(.netdev 및 .network) 재로드:

`networkctl reload`

- 네트워크 인터페이스 재구성 (구성을 편집한 경우, 먼저 `networkctl reload`를 호출해야 함):

`networkctl reconfigure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스1 인터페이스2 ...</span>
