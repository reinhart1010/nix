---
layout: page
title: common/palmtopnm (한국어)
description: "Palm 비트맵 파일을 PNM 이미지로 변환."
content_hash: 56e1fcbd6be359d3b51ef01893ce013ce1f7bcff
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/palmtopnm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# palmtopnm

Palm 비트맵 파일을 PNM 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/palmtopnm.html>.

- Palm 비트맵을 PNM 이미지로 변환:

`palmtopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.palm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pnm</span>

- 입력 파일에 대한 정보 표시:

`palmtopnm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.palm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pnm</span>

- 입력 파일에 포함된 이미지의 n번째 렌디션 변환:

`palmtopnm -rendition `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.palm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pnm</span>

- 입력 파일의 색상 히스토그램을 `stdout`에 출력:

`palmtopnm -showhist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.palm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pnm</span>

- 설정된 경우 입력 이미지의 투명 색상 출력:

`palmtopnm -transparent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.palm</span>
