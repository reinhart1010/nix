---
layout: page
title: common/arp (한국어)
description: "시스템의 ARP 캐시 표시 및 조작."
content_hash: 5d728a1a19c1149ebe0ef41050a7e7ce41c59ddd
related_topics:
  - title: English version
    url: /en/common/arp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/arp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/arp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp.html
    icon: bi bi-globe
---
# arp

시스템의 ARP 캐시 표시 및 조작.
더 많은 정보: <https://manned.org/arp>.

- 현재 arp 테이블을 보여줍니다:

`arp -a`

- 전체 캐시 삭제:

`sudo arp -a -d`

- 특정 엔트리 삭제:

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- 엔트리 생성:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>
