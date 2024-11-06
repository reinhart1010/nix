---
layout: page
title: common/pnmconvol (한국어)
description: "PNM 이미지를 컨볼루션."
content_hash: 21117c5659ef46ac6346bf0027d4c38d0e3b40e4
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmconvol.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmconvol

PNM 이미지를 컨볼루션.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmconvol.html>.

- 지정된 컨볼루션 행렬로 PNM 이미지 컨볼루션:

`pnmconvol -matrix=-1,3,-1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 입력 이미지의 각 레이어에 대해 파일로 지정된 컨볼루션 행렬로 PNM 이미지 컨볼루션:

`pnmconvol -matrixfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/행렬1,경로/대상/행렬2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 지정된 PNM 파일의 컨볼루션 행렬로 PNM 이미지 컨볼루션:

`pnmconvol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/행렬.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 컨볼루션 행렬의 가중치를 합이 1이 되도록 정규화:

`pnmconvol -matrix=-1,3,-1 -normalize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
