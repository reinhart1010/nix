---
layout: page
title: common/pnmcrop (한국어)
description: "PNM 이미지 자르기."
content_hash: 58415952498aa10dd64c14040105d8485e04a2fc
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmcrop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmcrop

PNM 이미지 자르기.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmcrop.html>.

- PNM 이미지의 흰색 테두리 제거:

`pnmcrop -white `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 지정한 색상의 상단 및 왼쪽 테두리 제거:

`pnmcrop -bg-color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상</span>` -top -left `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 지정한 코너의 픽셀 색상으로 제거할 테두리 색상 결정:

`pnmcrop -bg-corner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topleft|topright|bottomleft|bottomright</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- `n` 픽셀 너비의 테두리를 남김. 또한, 이미지가 배경으로만 이루어진 경우의 동작 지정:

`pnmcrop -margins `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -blank-image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pass|minimize|maxcrop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
