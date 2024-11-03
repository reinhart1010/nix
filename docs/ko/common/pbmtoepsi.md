---
layout: page
title: common/pbmtoepsi (한국어)
description: "PBM 이미지를 캡슐화된 PostScript 스타일의 미리보기 비트맵으로 변환."
content_hash: 4230933e952b43c61c3ad8caa2cd69e2c28978cd
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pbmtoepsi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbmtoepsi

PBM 이미지를 캡슐화된 PostScript 스타일의 미리보기 비트맵으로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtoepsi.html>.

- PBM 이미지를 캡슐화된 PostScript 스타일의 미리보기 비트맵으로 변환:

`pbmtoepsi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.bmp</span>

- 지정한 해상도로 정사각형 출력 이미지 생성:

`pbmtoepsi -dpi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">144</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.bmp</span>

- 지정한 가로 및 세로 해상도로 출력 이미지 생성:

`pbmtoepsi -dpi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">72x144</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.bmp</span>

- 경계 상자만 생성:

`pbmtoepsi -bbonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.bmp</span>
