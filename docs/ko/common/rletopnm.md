---
layout: page
title: common/rletopnm (한국어)
description: "Utah Raster Tools RLE 이미지 파일을 PNM 파일로 변환."
content_hash: 8b9af85152ed35cee36114f1c03e5bc9e1b536d2
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rletopnm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rletopnm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rletopnm

Utah Raster Tools RLE 이미지 파일을 PNM 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/rletopnm.html>.

- RLE 이미지를 PNM 파일로 변환:

`rletopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.rle</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- RLE 파일의 알파 채널을 포함하는 PGM 이미지 생성:

`rletopnm -alphaout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/알파_파일.pgm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.rle</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 자세한 모드로 작동하고 RLE 헤더의 내용을 `stdout`에 출력:

`rletopnm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.rle</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
