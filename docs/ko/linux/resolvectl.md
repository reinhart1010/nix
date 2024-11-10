---
layout: page
title: linux/resolvectl (한국어)
description: "도메인 이름, IPv4 및 IPv6 주소, DNS 리소스 레코드 및 서비스를 해석."
content_hash: 4e5783042ce9a40929512b33381cce322f90a9e3
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/resolvectl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/resolvectl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/resolvectl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/resolvectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# resolvectl

도메인 이름, IPv4 및 IPv6 주소, DNS 리소스 레코드 및 서비스를 해석.
DNS 해석기를 검사하고 재구성.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/resolvectl.html>.

- DNS 설정 표시:

`resolvectl status`

- 하나 이상의 도메인에 대한 IPv4 및 IPv6 주소 해석:

`resolvectl query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인1 도메인2 ...</span>

- 지정한 IP 주소의 도메인 검색:

`resolvectl query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소</span>

- 모든 로컬 DNS 캐시 플러시:

`resolvectl flush-caches`

- DNS 통계(트랜잭션, 캐시 및 DNSSEC 판결) 표시:

`resolvectl statistics`

- 도메인의 MX 레코드 검색:

`resolvectl --legend=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">no</span>` --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MX</span>` query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>

- 예를 들어 _xmpp-server._tcp gmail.com와 같은 SRV 레코드 해석:

`resolvectl service _`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스</span>`._`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로토콜</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- TLS 키 검색:

`resolvectl tlsa tcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>`:443`
