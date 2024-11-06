---
layout: page
title: common/pnmalias (한국어)
description: "PNM 이미지에 안티앨리어싱 적용."
content_hash: a01ee0d2a60da755677846ff95ab90b557a1337a
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmalias.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmalias

PNM 이미지에 안티앨리어싱 적용.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmalias.html>.

- PNM 이미지에 안티앨리어싱 적용, 검은 픽셀을 배경으로, 흰 픽셀을 전경으로 처리:

`pnmalias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 배경색과 전경색을 명시적으로 지정:

`pnmalias -bcolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배경_색상</span>` -fcolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">전경_색상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 전경 픽셀에만 안티앨리어싱 적용:

`pnmalias -fonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 배경 픽셀 주변의 모든 픽셀에 안티앨리어싱 적용:

`pnmalias -balias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>
