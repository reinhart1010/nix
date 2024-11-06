---
layout: page
title: common/pnmsmooth (한국어)
description: "PNM 이미지를 부드럽게 처리."
content_hash: cf24d2abd5e55c110e017c6698b8d967f617b0c8
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmsmooth.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmsmooth

PNM 이미지를 부드럽게 처리.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmsmooth.html>.

- 3x3 크기의 컨볼루션 행렬을 사용하여 PNM 이미지 부드럽게 처리:

`pnmsmooth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 가로 너비 x 세로 높이 크기의 컨볼루션 행렬을 사용하여 PNM 이미지 부드럽게 처리:

`pnmsmooth -width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>` -height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
