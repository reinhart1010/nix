---
layout: page
title: common/dhcpwn (한국어)
description: "DHCP IP 소진하는 공격을 테스트하고 로컬 DHCP 트래픽을 스니핑한다."
content_hash: c28289b74d6aa6769ac53291d0343f9f1b824cce
related_topics:
  - title: English version
    url: /en/common/dhcpwn.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dhcpwn.html
    icon: bi bi-globe
---
# dhcpwn

DHCP IP 소진하는 공격을 테스트하고 로컬 DHCP 트래픽을 스니핑한다.
더 많은 정보: <https://github.com/mschwager/dhcpwn>.

- 네트워크에 IP 요청들로 쇄도하기:

`dhcpwn --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_인터페이스</span>` flood --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">요청들의_수</span>

- 로컬 DHCP 트래픽 스니핑하기:

`dhcpwn --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_인터페이스</span>` sniff`
