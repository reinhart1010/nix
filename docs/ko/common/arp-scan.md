---
layout: page
title: common/arp-scan (한국어)
description: "ARP 패킷을 호스트(IP 주소 또는 호스트 이름으로 지정)로 보내 로컬 네트워크를 검색합니다."
content_hash: 945d0709d372879f193c1f84ecb8725a8f8d3100
last_modified_at: 2023-11-29
related_topics:
  - title: Deutsch version
    url: /de/common/arp-scan.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/arp-scan.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arp-scan.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arp-scan.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp-scan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arp-scan

ARP 패킷을 호스트(IP 주소 또는 호스트 이름으로 지정)로 보내 로컬 네트워크를 검색합니다.
더 많은 정보: <https://github.com/royhills/arp-scan>.

- 현재 로컬 네트워크 검색:

`arp-scan --localnet`

- 사용자 정의 비트마스크를 사용하여 IP 네트워크 스캔:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>

- 사용자 정의 범위 내에서 IP 네트워크 검색:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.0</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.31</span>

- 사용자 정의 넷 마스크로 IP 네트워크 스캔:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">255.255.255.0</span>
