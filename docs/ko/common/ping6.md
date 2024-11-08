---
layout: page
title: common/ping6 (한국어)
description: "IPv6 주소를 통해 네트워크 호스트에 ICMP ECHO_REQUEST 패킷을 전송."
content_hash: c18159b615fba6b59f0c8a62613c0f3912bcbd5a
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/common/ping6.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ping6.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ping6.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ping6.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping6

IPv6 주소를 통해 네트워크 호스트에 ICMP ECHO_REQUEST 패킷을 전송.
더 많은 정보: <https://manned.org/ping6>.

- 호스트에 핑:

`ping6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 호스트에 특정 횟수만큼 핑:

`ping6 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">횟수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 요청 간격을 초 단위로 지정하여 호스트에 핑 (기본값은 1초):

`ping6 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 주소에 대한 기호 이름을 조회하지 않고 호스트에 핑:

`ping6 -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 패킷을 수신할 때 벨 소리를 울리며 호스트에 핑 (터미널이 지원하는 경우):

`ping6 -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>
