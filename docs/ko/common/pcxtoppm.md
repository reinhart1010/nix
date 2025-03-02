---
layout: page
title: common/pcxtoppm (한국어)
description: "PCX 파일을 PPM 이미지로 변환."
content_hash: d613b243eb8b28328a2a50aa8a6a83dea4163adc
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pcxtoppm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pcxtoppm

PCX 파일을 PPM 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pcxtoppm.html>.

- PCX 파일을 PPM 이미지로 변환:

`pcxtoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcx</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>

- PCX 파일이 팔레트를 제공하더라도 미리 정의된 표준 팔레트를 사용:

`pcxtoppm -stdpalette `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcx</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>

- PCX 헤더 정보를 `stdout`에 출력:

`pcxtoppm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcx</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>
