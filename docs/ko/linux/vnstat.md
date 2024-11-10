---
layout: page
title: linux/vnstat (한국어)
description: "콘솔 기반 네트워크 트래픽 모니터."
content_hash: 3c01fa643fff0c2920778079a52dfdfbdba82f7f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/vnstat.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/vnstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vnstat

콘솔 기반 네트워크 트래픽 모니터.
더 많은 정보: <https://manned.org/vnstat>.

- 모든 인터페이스에 대한 트래픽 요약 표시:

`vnstat`

- 특정 네트워크 인터페이스에 대한 트래픽 요약 표시:

`vnstat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_인터페이스</span>

- 특정 네트워크 인터페이스에 대한 실시간 통계 표시:

`vnstat -l -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_인터페이스</span>

- 막대 그래프를 사용하여 지난 24시간 동안의 시간별 트래픽 통계 표시:

`vnstat -hg`

- 30초 동안 평균 트래픽 측정 및 표시:

`vnstat -tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
