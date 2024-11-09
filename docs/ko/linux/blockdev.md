---
layout: page
title: linux/blockdev (한국어)
description: "블록 장치를 관리, 조회 및 조작."
content_hash: 25fe36f7fae7ca6616efb8b631d9ac4de8cd5b3a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/blockdev.html
    icon: bi bi-globe
tldri18n_status: 2
---
# blockdev

블록 장치를 관리, 조회 및 조작.
더 많은 정보: <https://manned.org/blockdev>.

- 모든 장치에 대한 보고서 출력:

`sudo blockdev --report`

- 특정 장치에 대한 보고서 출력:

`sudo blockdev --report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- 장치의 크기를 512바이트 섹터 단위로 확인:

`sudo blockdev --getsz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- 읽기 전용으로 설정:

`sudo blockdev --setro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- 읽기-쓰기 가능으로 설정:

`sudo blockdev --setrw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- 버퍼 플러시:

`sudo blockdev --flushbufs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- 물리적 블록 크기 확인:

`sudo blockdev --getpbsz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- 선행 읽기 값을 128 섹터로 설정:

`sudo blockdev --setra 128 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>
