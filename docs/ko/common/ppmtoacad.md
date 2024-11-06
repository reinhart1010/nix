---
layout: page
title: common/ppmtoacad (한국어)
description: "PPM 이미지를 AutoCAD 데이터베이스 또는 슬라이드로 변환."
content_hash: 2ab35c8450f0b5e32509567d143b267ad1a29332
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmtoacad.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmtoacad

PPM 이미지를 AutoCAD 데이터베이스 또는 슬라이드로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoacad.html>.

- PPM 이미지를 AutoCAD 슬라이드로 변환:

`ppmtoacad `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.acad</span>

- PPM 이미지를 AutoCAD 바이너리 데이터베이스 가져오기 파일로 변환:

`ppmtoacad -dxb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.dxb</span>

- 출력의 색상을 8가지 RGB 음영으로 제한:

`ppmtoacad -8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.dxb</span>
