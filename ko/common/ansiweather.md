---
layout: page
title: common/ansiweather (한국어)
description: "당신의 터미널에서 현재 날씨 상태를 표시하는 쉘 스크립트."
content_hash: 7c503192f7afab593cf1d27cff2c35299ecbceab
related_topics:
  - title: English version
    url: /en/common/ansiweather.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansiweather.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansiweather.html
    icon: bi bi-globe
---
# ansiweather

당신의 터미널에서 현재 날씨 상태를 표시하는 쉘 스크립트.
더 많은 정보: <https://github.com/fcambus/ansiweather>.

- 폴란드 르제조에 대한 메트릭 단위를 사용하여 예측 표시:

`ansiweather -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metric</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rzeszow,PL</span>

- 당신의 현재 위치에 대한 기호 및 일광 데이터를 표시하는 예측 표시:

`ansiweather -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>

- 당신의 현재 위치의 바람과 습도 데이터를 보여주는 예측 표시:

`ansiweather -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>
