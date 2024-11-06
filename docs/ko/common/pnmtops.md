---
layout: page
title: common/pnmtops (한국어)
description: "PNM 이미지를 PostScript 파일로 변환."
content_hash: 7f0d99545b914481ddc2e621d62e7bc368b3d70b
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmtops.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmtops

PNM 이미지를 PostScript 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtops.html>.

- PNM 이미지를 PS 파일로 변환:

`pnmtops `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ps</span>

- 출력 이미지의 크기를 인치 단위로 지정:

`pnmtops -imagewidth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_너비</span>` -imageheight `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_높이</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ps</span>

- 출력 이미지가 위치할 페이지의 크기를 인치 단위로 지정:

`pnmtops -width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_너비</span>` -height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_높이</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ps</span>
