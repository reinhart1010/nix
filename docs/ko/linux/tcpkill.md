---
layout: page
title: linux/tcpkill (한국어)
description: "지정된 진행 중인 TCP 연결을 종료합니다."
content_hash: d576417bfe96b4054accb015d5f97bef55fb559f
last_modified_at: 2024-11-10
related_topics:
  - title: català version
    url: /ca/linux/tcpkill.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/tcpkill.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/tcpkill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tcpkill

지정된 진행 중인 TCP 연결을 종료합니다.
더 많은 정보: <https://manned.org/tcpkill>.

- 지정된 인터페이스, 호스트 및 포트에서 진행 중인 연결 종료:

`tcpkill -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>` host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.95.4.27</span>` and port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2266</span>
