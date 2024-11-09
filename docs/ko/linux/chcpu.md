---
layout: page
title: linux/chcpu (한국어)
description: "시스템의 CPU를 활성화/비활성화합니다."
content_hash: f583ba93f8bfd4afd3ba000509058a4951d81fce
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/chcpu.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/chcpu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chcpu

시스템의 CPU를 활성화/비활성화합니다.
더 많은 정보: <https://manned.org/chcpu>.

- 하나 이상의 CPU를 ID로 비활성화:

`chcpu -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,3</span>

- 하나 이상의 CPU 범위를 ID로 활성화:

`chcpu -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-3,5-7</span>
