---
layout: page
title: common/pamdeinterlace (한국어)
description: "Netpbm 이미지에서 격자 모양으로 행을 제거."
content_hash: f1082ba869ffdf4b08f3288fcd07b4ecd8537f5e
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pamdeinterlace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamdeinterlace

Netpbm 이미지에서 격자 모양으로 행을 제거.
같이 보기: `pammixinterlace`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamdeinterlace.html>.

- 입력 이미지의 짝수 행으로 구성된 이미지 생성:

`pamdeinterlace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 입력 이미지의 홀수 행으로 구성된 이미지 생성:

`pamdeinterlace -takeodd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>
