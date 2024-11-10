---
layout: page
title: linux/iwconfig (한국어)
description: "무선 네트워크 인터페이스의 매개변수를 구성하고 표시합니다."
content_hash: 229a256bb6481639b950b1a6c803f36528578331
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/iwconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iwconfig

무선 네트워크 인터페이스의 매개변수를 구성하고 표시합니다.
더 많은 정보: <https://manned.org/iwconfig>.

- 모든 인터페이스의 매개변수 및 통계 표시:

`iwconfig`

- 특정 인터페이스의 매개변수 및 통계 표시:

`iwconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 특정 인터페이스의 ESSID(네트워크 이름) 설정 (예: eth0 또는 wlp2s0):

`iwconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_네트워크_이름</span>

- 특정 인터페이스의 운영 모드 설정:

`iwconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Ad-Hoc|Managed|Master|Repeater|Secondary|Monitor|Auto</span>
