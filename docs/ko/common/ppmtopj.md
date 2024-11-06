---
layout: page
title: common/ppmtopj (한국어)
description: "PPM 파일을 HP PaintJet 파일로 변환."
content_hash: b434f6339b7e97b01e9fbc631b2d2196d5697f53
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmtopj.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmtopj

PPM 파일을 HP PaintJet 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtopj.html>.

- PPM 파일을 HP PaintJet 파일로 변환:

`ppmtopj `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pj</span>

- 이미지를 x 및 y 방향으로 이동:

`ppmtopj -xpos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dx</span>` -ypos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dy</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pj</span>

- 감마 값을 명시적으로 지정:

`ppmtopj -gamma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">감마</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pj</span>
