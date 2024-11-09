---
layout: page
title: linux/cbatticon (한국어)
description: "시스템 트레이에 위치하는 가볍고 빠른 배터리 아이콘."
content_hash: 36db7b75bead8d013454ad5b8f5af6d02a3f5300
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/cbatticon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cbatticon

시스템 트레이에 위치하는 가볍고 빠른 배터리 아이콘.
더 많은 정보: <https://github.com/valr/cbatticon>.

- 시스템 트레이에 배터리 아이콘 표시:

`cbatticon`

- 배터리 아이콘을 표시하고 업데이트 간격을 20초로 설정:

`cbatticon --update-interval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- 사용 가능한 아이콘 유형 나열:

`cbatticon --list-icon-types`

- 특정 아이콘 유형으로 배터리 아이콘 표시:

`cbatticon --icon-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">standard|notification|symbolic</span>

- 사용 가능한 전원 공급 장치 나열:

`cbatticon --list-power-supplies`

- 특정 배터리에 대한 배터리 아이콘 표시:

`cbatticon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">BAT0</span>

- 배터리 수준이 설정된 임계 수준에 도달했을 때 실행할 명령과 함께 배터리 아이콘 표시:

`cbatticon --critical-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` --command-critical-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poweroff</span>
