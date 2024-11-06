---
layout: page
title: common/pamdice (한국어)
description: "Netpbm 이미지를 수직 또는 수평으로 자르기."
content_hash: 0d5b0297990f83268d09dc009aef1a4f027a0b99
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pamdice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamdice

Netpbm 이미지를 수직 또는 수평으로 자르기.
같이 보기: `pamundice`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamdice.html>.

- 결과 타일이 지정된 높이와 너비를 가지도록 Netpbm 이미지 자르기:

`pamdice -outstem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명_스템</span>` -height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>

- 생성된 조각을 지정된 양만큼 수평 및 수직으로 겹치도록 만들기:

`pamdice -outstem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명_스템</span>` -height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -hoverlap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -voverlap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>
