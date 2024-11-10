---
layout: page
title: linux/tcpick (한국어)
description: "패킷 스니핑 및 네트워크 트래픽 분석 도구."
content_hash: b67176072b3561b82d96f7828c7ccfb89795b779
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/tcpick.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tcpick

패킷 스니핑 및 네트워크 트래픽 분석 도구.
TCP 연결 및 데이터를 캡처하고 표시할 수 있습니다. 또한 인터페이스, 호스트, 포트의 네트워크 트래픽을 모니터링할 수 있습니다.
더 많은 정보: <https://manned.org/tcpick.8>.

- 특정 [i]인터페이스, 포트 및 호스트의 트래픽 캡처:

`sudo tcpick -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` -C -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 특정 호스트의 포트 80(HTTP) 트래픽 캡처:

`sudo tcpick -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` -C -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.100</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- 도움말 표시:

`tcpick --help`
