---
layout: page
title: linux/ss (한국어)
description: "소켓을 조사하는 유틸리티."
content_hash: daefea364312b11d9a05881f7a37394bcb416b3a
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/ss.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ss

소켓을 조사하는 유틸리티.
더 많은 정보: <https://manned.org/ss.8>.

- 모든 TCP/UDP/RAW/UNIX 소켓 표시:

`ss -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|-u|-w|-x</span>

- 상태별로 TCP 소켓 필터링, 포함/제외:

`ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">state/exclude</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket/big/connected/synchronized/...</span>

- 로컬 HTTPS 포트(443)에 연결된 모든 TCP 소켓 표시:

`ss -t src :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443</span>

- 로컬 8080 포트에서 수신 중인 모든 TCP 소켓 표시:

`ss -lt src :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>

- 원격 SSH 포트에 연결된 프로세스와 함께 모든 TCP 소켓 표시:

`ss -pt dst :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh</span>

- 특정 소스 및 목적지 포트에 연결된 모든 UDP 소켓 표시:

`ss -u 'sport == :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_포트</span>` and dport == :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지_포트</span>`'`

- 서브넷 192.168.0.0/16에 로컬로 연결된 모든 TCP IPv4 소켓 표시:

`ss -4t src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168/16</span>

- 목적지 IP 192.168.1.17 및 목적지 포트 8080의 IPv4 또는 IPv6 소켓 연결 종료:

`ss --kill dst `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.17</span>` dport = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>
