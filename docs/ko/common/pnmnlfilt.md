---
layout: page
title: common/pnmnlfilt (한국어)
description: "PNM 이미지에 비선형 필터 적용."
content_hash: ecfd4ef7e0d7476cda92cb01ce678ae6343a7bd3
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmnlfilt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmnlfilt

PNM 이미지에 비선형 필터 적용.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmnlfilt.html>.

- 지정된 알파와 반경 값으로 "알파 트림 평균" 필터를 PNM 이미지에 적용:

`pnmnlfilt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0..0.5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">반경</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 지정된 노이즈 임계값과 반경으로 "최적 추정 스무딩" 필터를 PNM 이미지에 적용:

`pnmnlfilt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0..2.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">반경</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 지정된 알파와 반경으로 "엣지 향상" 필터를 PNM 이미지에 적용:

`pnmnlfilt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-0.9..(-0.1)</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">반경</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
