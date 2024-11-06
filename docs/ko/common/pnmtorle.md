---
layout: page
title: common/pnmtorle (한국어)
description: "PNM 파일을 Utah Raster Tools RLE 이미지 파일로 변환."
content_hash: 13bac4d971cdd9c322570d8fdf489caa8e25a02b
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmtorle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmtorle

PNM 파일을 Utah Raster Tools RLE 이미지 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtorle.html>.

- PNM 이미지를 RLE 이미지로 변환:

`pnmtorle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.rle</span>

- PNM 헤더 정보를 `stdout`에 출력:

`pnmtorle -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.rle</span>

- 출력 이미지에 투명 채널 포함, 모든 검은색 픽셀은 완전히 투명하게, 다른 모든 픽셀은 완전히 불투명하게 설정:

`pnmtorle -alpha `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.rle</span>
