---
layout: page
title: common/ppmdither (한국어)
description: "디더링을 적용하여 이미지의 색상 수를 줄입니다."
content_hash: e14a806cd256c36f332f16d77828583243b282c9
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmdither.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmdither

디더링을 적용하여 이미지의 색상 수를 줄입니다.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmdither.html>.

- PPM 이미지를 읽고 디더링을 적용하여 파일로 저장:

`ppmdither `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>

- 각 기본 색상에 대한 원하는 음영 수 지정:

`ppmdither -red `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -green `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -blue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>

- 디더링 행렬의 크기 지정:

`ppmdither -dim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>
