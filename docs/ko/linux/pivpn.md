---
layout: page
title: linux/pivpn (한국어)
description: "보안이 강화된 OpenVPN을 쉽게 설정하고 관리하는 도구."
content_hash: 49ae1ed3fb37b17c971d10bfc10efb9636ab4963
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pivpn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pivpn

보안이 강화된 OpenVPN을 쉽게 설정하고 관리하는 도구.
원래는 Raspberry Pi를 위해 설계되었지만, 다른 Linux 장치에서도 작동합니다.
더 많은 정보: <https://www.pivpn.io/>.

- 새로운 클라이언트 장치 추가:

`sudo pivpn add`

- 모든 클라이언트 장치 나열:

`sudo pivpn list`

- 현재 연결된 장치 및 그 통계 나열:

`sudo pivpn clients`

- 이전에 인증된 장치 해제:

`sudo pivpn revoke`

- PiVPN 제거:

`sudo pivpn uninstall`
