---
layout: page
title: common/traceroute (한국어)
description: "네트워크 호스트로 패킷 경로를 추적하여 출력."
content_hash: ddd1908779d69860befb48ce98e341f3c71352ea
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/traceroute.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/traceroute.html
    icon: bi bi-globe
tldri18n_status: 2
---
# traceroute

네트워크 호스트로 패킷 경로를 추적하여 출력.
더 많은 정보: <https://manned.org/traceroute>.

- 호스트로 traceroute 실행:

`traceroute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- IP 주소 및 호스트 이름 매핑 비활성화:

`traceroute -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 응답 대기 시간을 초 단위로 지정:

`traceroute --wait=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 홉당 쿼리 수 지정:

`traceroute --queries=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 프로빙 패킷의 크기를 바이트 단위로 지정:

`traceroute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- 목적지까지의 MTU 결정:

`traceroute --mtu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- UDP 대신 ICMP를 사용하여 traceroute 실행:

`traceroute --icmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
