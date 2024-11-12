---
layout: page
title: osx/ping (한국어)
description: "네트워크 호스트에 ICMP ECHO_REQUEST 패킷을 전송합니다."
content_hash: 10801b13f4ba1dcb6bd1f1c36e16171a792100aa
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/ping.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/ping.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/ping.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/ping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping

네트워크 호스트에 ICMP ECHO_REQUEST 패킷을 전송합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/ping.8.html>.

- 지정된 호스트에 핑 보내기:

`ping "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>`"`

- 호스트에 특정 횟수만큼 핑 보내기:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">횟수</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`"`

- 요청 간격을 초 단위로 지정하여 호스트에 핑 보내기 (기본값은 1초):

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`"`

- 주소에 대한 기호 이름을 조회하지 않고 호스트에 핑 보내기:

`ping -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`"`

- 호스트에 핑을 보내고 패킷을 수신했을 때 벨을 울리기 (터미널이 지원하는 경우):

`ping -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`"`

- 호스트에 핑을 보내고 패킷을 수신한 시간을 표시하기 (이 옵션은 Apple 추가 기능입니다):

`ping --apple-time "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`"`
