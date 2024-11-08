---
layout: page
title: common/redshift (한국어)
description: "주변 환경에 따라 화면의 색온도를 조정."
content_hash: 6f6ede1f699a80a6aa383c9cc190bd707781941a
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/redshift.html
    icon: bi bi-globe
tldri18n_status: 2
---
# redshift

주변 환경에 따라 화면의 색온도를 조정.
더 많은 정보: <http://jonls.dk/redshift>.

- 낮 동안 특정 [t]온도(예: 5700K)와 밤 동안 특정 온도(예: 3600K)로 Redshift 켜기:

`redshift -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5700</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- 수동으로 지정한 맞춤 [l]위치로 Redshift 켜기:

`redshift -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">위도</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경도</span>

- 낮 동안 특정 화면 [b]밝기(예: 70%)와 밤 동안 특정 밝기(예: 40%)로 Redshift 켜기:

`redshift -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.7</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.4</span>

- 맞춤 [g]감마 수준(0과 1 사이)으로 Redshift 켜기:

`redshift -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">green</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>

- 기존의 온도 변화를 [P]제거하고 [O]ne-shot 모드에서 일정한 색온도를 설정:

`redshift -PO `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">온도</span>
