---
layout: page
title: common/ansiweather (한국어)
description: "당신의 터미널에서 현재 날씨 상태를 표시하는 쉘 스크립트."
content_hash: 0ad5e4d5d494338960efa69cc86261fcffc7283a
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/ansiweather.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansiweather.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansiweather.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansiweather.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ansiweather.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansiweather.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansiweather.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansiweather

당신의 터미널에서 현재 날씨 상태를 표시하는 쉘 스크립트.
더 많은 정보: <https://github.com/fcambus/ansiweather>.

- 폴란드 르제조에 대한 메트릭 단위를 사용하여 예측 표시:

`ansiweather -u metric -f 7 -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rzeszow,PL</span>

- 당신의 현재 위치에 대한 기호 및 일광 데이터를 표시하는 예측 표시:

`ansiweather -F -s true -d true`

- 당신의 현재 위치의 바람과 습도 데이터를 보여주는 예측 표시:

`ansiweather -w true -h true`
