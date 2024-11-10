---
layout: page
title: common/tifftopnm (한국어)
description: "TIFF 이미지를 PNM 이미지로 변환."
content_hash: 86ca440610d966f3dda9badd6614373ae695a9ad
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tifftopnm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tifftopnm

TIFF 이미지를 PNM 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/tifftopnm.html>.

- TIFF를 PNM 파일로 변환:

`tifftopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.tiff</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.pnm</span>

- 입력 이미지의 알파 채널을 포함하는 PGM 파일 생성:

`tifftopnm -alphaout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/알파_파일.pgm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.tiff</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.pnm</span>

- 입력 TIFF 이미지의 `fillorder` 태그 고려:

`tifftopnm -respectfillorder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.tiff</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.pnm</span>

- TIFF 헤더 정보를 `stderr`에 출력:

`tifftopnm -headerdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.tiff</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.pnm</span>
