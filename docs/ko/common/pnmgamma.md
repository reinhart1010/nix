---
layout: page
title: common/pnmgamma (한국어)
description: "PNM 이미지에 감마 보정 수행."
content_hash: 18940887f68bc24990a82c2c1c2347270a02f500
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmgamma.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmgamma

PNM 이미지에 감마 보정 수행.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmgamma.html>.

- 이미지를 BT.709 휘도에서 방사선 또는 sRGB 휘도로 변환:

`pnmgamma -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bt709tolinear|bt709tosrgb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 이미지를 방사선 또는 sRGB 휘도에서 BT.709 휘도로 변환:

`pnmgamma -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lineartobt709|srgbtobt709</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 감마 전송 함수에 사용될 감마 값 지정:

`pnmgamma -gamma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 색 구성 요소별로 감마 전송 함수에 사용될 감마 값 지정:

`pnmgamma -rgamma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -ggamma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -bgamma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
