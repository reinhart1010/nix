---
layout: page
title: common/dhclient (한국어)
description: "DHCP 클라이언트."
content_hash: d68676bfdd4c996e79e35292fa74687e10db1f6f
related_topics:
  - title: English version
    url: /en/common/dhclient.html
    icon: bi bi-globe
---
# dhclient

DHCP 클라이언트.
더 많은 정보: <https://manned.org/dhclient>.

- 'eht0' 인터페이스의 IP 주소 얻기:

`sudo dhclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 'eth0' 인터페이스의 IP 주소 해제하기:

`sudo dhclient -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>
