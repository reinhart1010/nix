---
layout: page
title: netbsd/sockstat (한국어)
description: "열린 인터넷 또는 UNIX 도메인 소켓을 나열합니다."
content_hash: e12379b8d9f7ec488000f04e1b5223d83cab80a1
last_modified_at: 2024-09-19
related_topics:
  - title: English version
    url: /en/netbsd/sockstat.html
    icon: bi bi-globe
  - title: español version
    url: /es/netbsd/sockstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/sockstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sockstat

열린 인터넷 또는 UNIX 도메인 소켓을 나열합니다.
참고: 이 프로그램은 FreeBSD의 `sockstat`를 NetBSD 3.0용으로 다시 작성한 것입니다.
같이 보기: `netstat`.
더 많은 정보: <https://man.netbsd.org/sockstat.1>.

- IPv4, IPv6 및 Unix 소켓에 대한 수신 및 연결된 소켓에 대한 정보 표시:

`sockstat`

- 특정 포트에서 특정 프로토콜을 사용하는 IPv[4]/IPv[6] 소켓 [l]istening에 대한 정보 표시:

`sockstat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>` -l -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|sctp|divert</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2...</span>

- [c]onnected 소켓도 표시하며 [u]nix 소켓도 표시:

`sockstat -cu`

- 주소 및 포트의 심볼릭 이름을 해결하지 않고 [n]umeric 출력만 표시:

`sockstat -n`

- 지정된 주소 [f]amily의 소켓만 나열:

`sockstat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inet|inet6|local|unix</span>
