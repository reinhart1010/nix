---
layout: page
title: common/piactl (한국어)
description: "상업용 VPN 제공업체인 Private Internet Access의 명령줄 도구."
content_hash: bab2722a64e01bfac43c5ec0d2a227ef872e7444
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/piactl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# piactl

상업용 VPN 제공업체인 Private Internet Access의 명령줄 도구.
더 많은 정보: <https://helpdesk.privateinternetaccess.com/kb/articles/pia-desktop-command-line-interface-part-1>.

- Private Internet Access에 로그인:

`piactl login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로그인_파일</span>

- Private Internet Access에 연결:

`piactl connect`

- Private Internet Access에서 연결 해제:

`piactl disconnect`

- 백그라운드에서 Private Internet Access 데몬 활성화 또는 비활성화:

`piactl background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>

- 사용 가능한 모든 VPN 지역 나열:

`piactl get regions`

- 현재 VPN 지역 표시:

`piactl get region`

- VPN 지역 설정:

`piactl set region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지역</span>

- Private Internet Access에서 로그아웃:

`piactl logout`
