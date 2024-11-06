---
layout: page
title: common/ppmhist (한국어)
description: "PPM 이미지에 포함된 색상의 히스토그램을 출력."
content_hash: 0291278bf37905e078b610af374881708f704cbe
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmhist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmhist

PPM 이미지에 포함된 색상의 히스토그램을 출력.
같이 보기: `pgmhist`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmhist.html>.

- 사람이 읽을 수 있는 형식으로 히스토그램 생성:

`ppmhist -nomap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>

- 이미지의 색상 히스토그램을 주석으로 포함한 컬러맵의 PPM 파일 생성:

`ppmhist -map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>

- 버전 표시:

`ppmhist -version`
