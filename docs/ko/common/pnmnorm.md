---
layout: page
title: common/pnmnorm (한국어)
description: "PNM 이미지의 대비를 정규화합니다."
content_hash: 16b076bfa0aa39df8da7e6fbfc3d1e3199c9a1d2
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmnorm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pnmnorm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pnmnorm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmnorm

PNM 이미지의 대비를 정규화합니다.
같이 보기: `pnmhisteq`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmnorm.html>.

- 가장 밝은 픽셀을 흰색으로, 가장 어두운 픽셀을 검은색으로 설정하고 그 사이의 픽셀을 선형적으로 분포시키기:

`pnmnorm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 가장 밝은 픽셀을 흰색으로, 가장 어두운 픽셀을 검은색으로 설정하고 그 사이의 픽셀을 n의 밝기로 50% 밝게 되도록 이차적으로 분포시키기:

`pnmnorm -midvalue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 픽셀의 색조는 유지하고 밝기만 수정하기:

`pnmnorm -keephues `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 픽셀의 밝기를 계산하는 방법 지정하기:

`pnmnorm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">luminosity|colorvalue|saturation</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
