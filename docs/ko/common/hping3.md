---
layout: page
title: common/hping3 (한국어)
description: "TCP, UDP 및 원시 IP와 같은 프로토콜을 지원하는 고급 ping 유틸리티."
content_hash: 8e73d5ed7576e71439d8a5e8ec6781bee5f07d42
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/hping3.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/hping3.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hping3.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hping3

TCP, UDP 및 원시 IP와 같은 프로토콜을 지원하는 고급 ping 유틸리티.
높은 권한으로 실행하는 것이 가장 좋음.
더 많은 정보: <https://github.com/antirez/hping>.

- 4개의 ICMP ping 요청으로 대상에 ping을 보냄:

`hping3 --icmp --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_또는_호스트명</span>

- 포트 80에서 UDP를 통해 IP 주소를 ping:

`hping3 --udp --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --syn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_또는_호스트명</span>

- 특정 로컬 소스 포트 5090에서 스캔해 TCP 포트 80을 스캔:

`hping3 --verbose --syn --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --baseport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5090</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_또는_호스트명</span>

- 특정 대상 포트에 대한 TCP 스캔을 사용해 경로를 추적:

`hping3 --traceroute --verbose --syn --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_또는_호스트명</span>

- 특정 IP 주소에서 TCP 포트 세트를 스캔 :

`hping3 --scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,3000,9000</span>` --syn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_또는_호스트명</span>

- TCP ACK 스캔을 수행해, 특정 호스트가 살아 있는지 확인:

`hping3 --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --verbose --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --ack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_또는_호스트명</span>

- 포트 80에서 부하 테스트를 수행:

`hping3 --flood --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --syn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_또는_호스트명</span>
