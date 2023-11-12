---
layout: page
title: common/tcpdump (한국어)
description: "네트워크의 트래픽 덤프."
content_hash: 3ece0f8409ce165d3797624556b0fee8efedc863
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/tcpdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tcpdump

네트워크의 트래픽 덤프.
더 많은 정보: <https://www.tcpdump.org>.

- 사용 가능한 네트워크 인터페이스 나열:

`tcpdump -D`

- 특정 인터페이스의 트래픽 캡처:

`tcpdump -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 콘솔에서 콘텐츠(ASCII)를 표시하는 모든 TCP 트래픽을 캡처:

`tcpdump -A tcp`

- 호스트에서 들어오고 나가는 트래픽을 캡처:

`tcpdump host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- 특정 인터페이스, 소스, 목적지 및 목적지 포트에서 트래픽을 캡처:

`tcpdump -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>` and dst `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.2</span>` and dst port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- 네트워크 트래픽 캡처:

`tcpdump net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.0/24</span>

- 포트 22를 통한 트래픽을 제외한 모든 트래픽을 캡처하고 덤프 파일에 저장:

`tcpdump -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dumpfile.pcap</span>` port not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- 지정된 덤프 파일에서 읽기:

`tcpdump -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dumpfile.pcap</span>
