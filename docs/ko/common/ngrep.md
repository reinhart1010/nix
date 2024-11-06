---
layout: page
title: common/ngrep (한국어)
description: "정규식을 사용하여 네트워크 트래픽 패킷을 필터링."
content_hash: fa2e991e57620d207cbadb53d9c4ceeede2d43d5
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ngrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ngrep

정규식을 사용하여 네트워크 트래픽 패킷을 필터링.
더 많은 정보: <https://github.com/jpr5/ngrep>.

- 모든 인터페이스의 트래픽 캡처:

`ngrep -d any`

- 특정 인터페이스의 트래픽 캡처:

`ngrep -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 인터페이스 eth0의 포트 22를 지나는 트래픽 캡처:

`ngrep -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- 특정 호스트로부터 또는 특정 호스트로 가는 트래픽 캡처:

`ngrep host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- 인터페이스 eth0의 'User-Agent:' 키워드 필터링:

`ngrep -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">User-Agent:</span>`'`
