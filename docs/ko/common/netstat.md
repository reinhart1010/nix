---
layout: page
title: common/netstat (한국어)
description: "네트워크 관련 정보(열려 있는 연결, 소켓 포트 등) 표시."
content_hash: 327acfc74e557c82bbac58a30fb6089ac029e6b4
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/netstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/netstat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/netstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# netstat

네트워크 관련 정보(열려 있는 연결, 소켓 포트 등) 표시.
같이 보기: `ss`.
더 많은 정보: <https://manned.org/netstat>.

- 모든 포트 나열:

`netstat --all`

- 수신 대기 중인 모든 포트 나열:

`netstat --listening`

- 수신 대기 중인 TCP 포트 나열:

`netstat --tcp`

- PID 및 프로그램 이름 표시:

`netstat --program`

- 정보를 지속적으로 나열:

`netstat --continuous`

- 경로를 나열하고 IP 주소를 호스트 이름으로 변환하지 않음:

`netstat --route --numeric`

- 수신 대기 중인 TCP 및 UDP 포트 나열 (+ 루트 권한일 경우 사용자 및 프로세스 표시):

`netstat --listening --program --numeric --tcp --udp --extend`
