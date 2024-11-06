---
layout: page
title: common/pnmrotate (한국어)
description: "PNM 이미지를 회전."
content_hash: 215cc9963a4e81e300954490d72fec5729f59a10
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmrotate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmrotate

PNM 이미지를 회전.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmrotate.html>.

- PNM 이미지를 특정 각도(도 단위, 반시계 방향)로 회전:

`pnmrotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">각도</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 입력 이미지를 회전할 때 노출되는 배경색 지정:

`pnmrotate -background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">각도</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 성능을 향상시키지만 품질이 감소하는 안티앨리어싱 비활성화:

`pnmrotate -noantialias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">각도</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
