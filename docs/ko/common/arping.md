---
layout: page
title: common/arping (한국어)
description: "ARP 프로토콜을 사용하여 네트워크에서 호스트를 발견하고 탐색합니다."
content_hash: f9a3ead3a0d76455612353e0ff65bf91b1594f8f
related_topics:
  - title: English version
    url: /en/common/arping.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/arping.html
    icon: bi bi-globe
---
# arping

ARP 프로토콜을 사용하여 네트워크에서 호스트를 발견하고 탐색합니다.
MAC 주소 검색에 유용합니다.
더 많은 정보: <https://github.com/ThomasHabets/arping>.

- ARP 요청 패킷으로 호스트 ping 하기:

`arping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- 특정 인터페이스의 호스트로 ping 하기:

`arping -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- 첫 응답을 한 호스트로 ping 하기:

`arping -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- 호스트에 특정 횟수 ping 하기:

`arping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- 브로드캐스트 ARP 요청 패킷을 통해 이웃 ARP 캐시 업데이트:

`arping -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_to_broadcast</span>

- 3초의 시간 제한을 사용하여 ARP 요청을 전송하여 네트워크에서 중복된 IP 주소를 탐지합니다:

`arping -D -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_to_check</span>
