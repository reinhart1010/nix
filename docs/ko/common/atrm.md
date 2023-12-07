---
layout: page
title: common/atrm (한국어)
description: "`at` 또는 `batch` 명령으로 예약된 작업 제거."
content_hash: ea4d9ce6870bca808b98e0ceb2974e9ca38fd179
last_modified_at: 2023-12-07
related_topics:
  - title: English version
    url: /en/common/atrm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atrm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atrm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atrm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atrm

`at` 또는 `batch` 명령으로 예약된 작업 제거.
작업 번호를 찾으려면 `atq`를 사용하세요.
더 많은 정보: <https://manned.org/atrm>.

- 작업 번호 10 제거:

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 공백으로 구분된 여러 작업 제거:

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>
