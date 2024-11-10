---
layout: page
title: linux/tcptraceroute (한국어)
description: "TCP 패킷을 사용하는 traceroute 구현."
content_hash: bf484e4faed73ed86c7784b4e1bc48f46bc0fa3b
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/tcptraceroute.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tcptraceroute

TCP 패킷을 사용하는 traceroute 구현.
더 많은 정보: <https://github.com/mct/tcptraceroute>.

- 호스트까지의 경로 추적:

`tcptraceroute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 목적지 포트와 패킷 길이(바이트 단위) 지정:

`tcptraceroute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지_포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패킷_길이</span>

- 로컬 소스 포트와 소스 주소 지정:

`tcptraceroute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_포트</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_주소</span>

- 첫 번째 및 최대 TTL 설정:

`tcptraceroute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">첫번째_ttl</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_ttl</span>

- 대기 시간과 홉당 쿼리 수 지정:

`tcptraceroute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대기_시간</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리_수</span>

- 인터페이스 지정:

`tcptraceroute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>
