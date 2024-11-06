---
layout: page
title: common/pnmhisteq (한국어)
description: "PNM 이미지의 히스토그램을 균등화."
content_hash: 84f3f9fb7dbbdc9d450d16c446b80b109c94384a
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmhisteq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmhisteq

PNM 이미지의 히스토그램을 균등화.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmhisteq.html>.

- 히스토그램 균등화를 사용하여 PNM 이미지의 대비 증가:

`pnmhisteq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 회색 픽셀만 수정:

`pnmhisteq -grey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 히스토그램 균등화에서 검정 또는 흰색 픽셀 제외:

`pnmhisteq -no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">black|white</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
