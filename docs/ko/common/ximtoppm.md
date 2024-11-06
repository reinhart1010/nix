---
layout: page
title: common/ximtoppm (한국어)
description: "XIM 파일을 PPM 이미지로 변환."
content_hash: b97458709e231a47429482db5b85b3f5b5fca3be
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ximtoppm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ximtoppm

XIM 파일을 PPM 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ximtoppm.html>.

- XIM 이미지를 PPM 이미지로 변환:

`ximtoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.xim</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>

- 입력 이미지의 투명 마스크를 지정된 파일에 저장:

`ximtoppm --alphaout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/알파_파일.pbm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.xim</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>
