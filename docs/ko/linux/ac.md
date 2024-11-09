---
layout: page
title: linux/ac (한국어)
description: "사용자가 얼마나 오랫동안 연결되어 있었는지에 대한 통계를 출력합니다."
content_hash: 0129b9da681a0e57aa801efd95061b000b224cfc
last_modified_at: 2024-11-09
related_topics:
  - title: català version
    url: /ca/linux/ac.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ac.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/ac.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/ac.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ac.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ac

사용자가 얼마나 오랫동안 연결되어 있었는지에 대한 통계를 출력합니다.
더 많은 정보: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- 현재 사용자가 몇 시간 동안 연결되었는지 출력:

`ac`

- 사용자가 몇 시간 동안 연결되었는지 출력:

`ac --individual-totals`

- 특정 사용자가 몇 시간 동안 연결되었는지 출력:

`ac --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 특정 사용자가 하루 동안 몇 시간 연결되었는지 출력(총합 포함):

`ac --daily-totals --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 추가 세부 정보도 표시:

`ac --compatibility`
