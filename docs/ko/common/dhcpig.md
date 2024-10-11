---
layout: page
title: common/dhcpig (한국어)
description: "고급 DHCP 자원 고갈 공격 및 스트레스 테스트를 시작."
content_hash: a0a1210f76a77fd9a750e1e5189ece4f033344db
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/dhcpig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dhcpig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dhcpig

고급 DHCP 자원 고갈 공격 및 스트레스 테스트를 시작.
DHCPig은 루트 권한으로 실행해야 함.
더 많은 정보: <https://github.com/kamorin/DHCPig>.

- 지정된 인터페이스를 사용하여 사용 가능한 DHCP 주소를 소진:

`sudo ./pig.py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- eth1 인터페이스를 사용하여 IPv6를 고갈 :

`sudo ./pig.py -6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>

- 인터페이스를 사용하여 퍼지/잘못된 데이터 패킷을 전송:

`sudo ./pig.py --fuzz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>

- 색상 출력 활성화:

`sudo ./pig.py -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>

- 최소한의 장황함과 색상 출력을 활성화:

`sudo ./pig.py -c --verbosity=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>

- 디버그 상세 출력 수준을 100으로 하고 ARP 패킷을 사용해 장치 근처 네트워크를 검색:

`sudo ./pig.py -c --verbosity=100 --neighbors-scan-arp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>

- 임대 정보 출력을 활성화하고, 모든 근처 IP 주소를 검색하고 해제하려 시도:

`sudo ./pig.py --neighbors-scan-arp -r --show-options `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>
