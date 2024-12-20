---
layout: page
title: linux/ethtool (한국어)
description: "네트워크 인터페이스 컨트롤러(NIC) 매개변수를 표시하고 수정합니다."
content_hash: d49b2c0d698506e65bdadbc6a7a674870a38981b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ethtool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ethtool

네트워크 인터페이스 컨트롤러(NIC) 매개변수를 표시하고 수정합니다.
더 많은 정보: <https://manned.org/ethtool>.

- 인터페이스의 현재 설정 표시:

`ethtool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 인터페이스의 드라이버 정보 표시:

`ethtool --driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 인터페이스에서 지원되는 모든 기능 표시:

`ethtool --show-features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 인터페이스의 네트워크 사용 통계 표시:

`ethtool --statistics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 인터페이스의 하나 이상의 LED를 10초 동안 깜박이기:

`ethtool --identify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 주어진 인터페이스의 링크 속도, 이중 모드 및 매개변수 자동 협상 설정:

`ethtool -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10|100|1000</span>` duplex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">half|full</span>` autoneg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>
