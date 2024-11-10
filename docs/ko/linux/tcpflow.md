---
layout: page
title: linux/tcpflow (한국어)
description: "TCP 트래픽을 캡처하여 디버깅 및 분석합니다."
content_hash: 6864a185d50ed86184b93921fb331495f14c8d4f
last_modified_at: 2024-11-10
related_topics:
  - title: català version
    url: /ca/linux/tcpflow.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/tcpflow.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/tcpflow.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/tcpflow.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tcpflow

TCP 트래픽을 캡처하여 디버깅 및 분석합니다.
더 많은 정보: <https://manned.org/tcpflow>.

- 특정 인터페이스와 포트의 모든 데이터 표시:

`tcpflow -c -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>
