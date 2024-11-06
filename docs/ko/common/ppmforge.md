---
layout: page
title: common/ppmforge (한국어)
description: "구름, 행성 및 별이 빛나는 하늘과 같은 프랙탈을 생성합니다."
content_hash: 70919d2c212e76fd83e4ccbe7bba75e52352f063
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmforge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmforge

구름, 행성 및 별이 빛나는 하늘과 같은 프랙탈을 생성합니다.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmforge.html>.

- 행성 이미지를 생성:

`ppmforge > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>

- 구름이나 밤하늘 이미지를 생성:

`ppmforge -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">night|clouds</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>

- 프랙탈 생성에 사용자 정의 메쉬 크기와 차원을 사용하고 출력의 크기를 지정:

`ppmforge -mesh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` -dimension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.5</span>` -xsize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000</span>` -ysize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>

- 생성된 행성의 기울기 및 조명 각도 조절:

`ppmforge -tilt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-15</span>` -hour `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>
