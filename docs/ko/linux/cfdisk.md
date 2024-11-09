---
layout: page
title: linux/cfdisk (한국어)
description: "curses UI를 사용하여 하드 디스크의 파티션 테이블 및 파티션을 관리."
content_hash: 1df1dd875896f3d8b590d1b5946cb6a2f0c6c503
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/linux/cfdisk.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/cfdisk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/cfdisk.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/cfdisk.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cfdisk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cfdisk

curses UI를 사용하여 하드 디스크의 파티션 테이블 및 파티션을 관리.
더 많은 정보: <https://manned.org/cfdisk>.

- 특정 장치로 파티션 조작기 시작:

`cfdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 특정 장치에 대한 새 파티션 테이블 생성 및 관리:

`cfdisk --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
