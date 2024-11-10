---
layout: page
title: linux/hwclock (한국어)
description: "하드웨어 시계를 읽거나 변경합니다. 일반적으로 루트 권한이 필요합니다."
content_hash: 7147ec914b5fb5d4a59e5c26947dd1d405cc9a12
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/hwclock.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hwclock

하드웨어 시계를 읽거나 변경합니다. 일반적으로 루트 권한이 필요합니다.
더 많은 정보: <https://manned.org/hwclock>.

- 하드웨어 시계에 의해 보고된 현재 시간 표시:

`hwclock`

- 현재 소프트웨어 시계 시간을 하드웨어 시계에 기록 (시스템 설정 중에 사용되기도 함):

`hwclock --systohc`

- 현재 하드웨어 시계 시간을 소프트웨어 시계에 기록:

`hwclock --hctosys`
