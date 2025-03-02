---
layout: page
title: common/chronyc (한국어)
description: "Chrony NTP 데몬을 쿼리합니다."
content_hash: 568d4c8e85caa8f7d734be1c7c5e53a5cc56dbd2
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/chronyc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chronyc

Chrony NTP 데몬을 쿼리합니다.
더 많은 정보: <https://chrony-project.org/doc/4.6.1/chronyc.html>.

- 대화형 모드로 `chronyc` 시작:

`chronyc`

- Chrony 데몬의 추적 통계 표시:

`chronyc tracking`

- Chrony가 현재 사용 중인 시간 소스 출력:

`chronyc sources`

- Chrony 데몬이 현재 시간 소스로 사용 중인 소스의 통계 표시:

`chronyc sourcestats`

- 시스템 시계를 즉시 조정하여 슬루를 우회:

`chronyc makestep`

- 각 NTP 소스에 대한 자세한 정보 표시:

`chronyc ntpdata`
