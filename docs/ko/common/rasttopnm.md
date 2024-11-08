---
layout: page
title: common/rasttopnm (한국어)
description: "Sun 래스터 파일을 PNM 파일로 변환."
content_hash: e06deed22c507e00d5cb5f2ea889e654dc491c90
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rasttopnm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rasttopnm

Sun 래스터 파일을 PNM 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/rasttopnm.html>.

- RAST 이미지를 PNM 파일로 변환:

`rasttopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.rast</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 색상 값이 있는 경우 래스터의 색상 맵 인덱스를 사용:

`rasttopnm -index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.rast</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
