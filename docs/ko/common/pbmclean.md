---
layout: page
title: common/pbmclean (한국어)
description: "PBM 이미지를 정리하여 고립된 검은색 및 흰색 픽셀을 제거합니다."
content_hash: 06c188afb970b2e6c8ee4fa24a90490883aa6569
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pbmclean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbmclean

PBM 이미지를 정리하여 고립된 검은색 및 흰색 픽셀을 제거합니다.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmclean.html>.

- 고립된 검은색 및 흰색 픽셀을 제거하여 PBM 이미지 정리:

`pbmclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 검은색/흰색 픽셀만 정리:

`pbmclean -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">black|white</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 고립되지 않은 픽셀로 간주되기 위한 최소한의 동일 색상 이웃 픽셀 수 지정:

`pbmclean -minneighbours `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>
