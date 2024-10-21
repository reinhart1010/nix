---
layout: page
title: common/fitstopnm (한국어)
description: "FITS(Flexible Image Transport System) 파일을 PNM 이미지로 변환."
content_hash: 54d63a2ee4bd1a20ea585cf1af0be5193fecf4a2
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/fitstopnm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fitstopnm

FITS(Flexible Image Transport System) 파일을 PNM 이미지로 변환.
참조: `pamtofits`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/fitstopnm.html>.

- FITS 파일을 PNM 이미지로 변환:

`fitstopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.fits</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.pnm</span>

- FITS 파일의 세 번째 축의 지정된 위치에서 이미지를 변환:

`fitstopnm -image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">z_position</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.fits</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.pnm</span>
