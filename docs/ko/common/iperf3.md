---
layout: page
title: common/iperf3 (한국어)
description: "네트워크 대역폭 테스트를 위한 트래픽 생성기입니다."
content_hash: 1f19cfc85caad442198e38dc2d85d945a35756e7
last_modified_at: 2023-10-20
related_topics:
  - title: English version
    url: /en/common/iperf3.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># iperf3

네트워크 대역폭 테스트를 위한 트래픽 생성기입니다.
더 많은 정보: <https://iperf.fr>.

- iperf3를 서버로 실행:

`iperf3 -s`

- 특정 포트에서 iperf3 서버 실행:

`iperf3 -s -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 대역폭 테스트 시작:

`iperf3 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>

- 여러 병렬 스트림에서 iperf3 실행:

`iperf3 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스트림</span>

- 테스트를 역방향으로 진행합니다. 서버가 클라이언트에 데이터를 전송:

`iperf3 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>` -R`
