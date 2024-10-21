---
layout: page
title: common/gammastep (한국어)
description: "하루 중 시간에 따라 화면의 색온도를 조정."
content_hash: 9fd468134e9bc6c08af65582b0f6bd20c5241321
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gammastep.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/gammastep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Gammastep

하루 중 시간에 따라 화면의 색온도를 조정.
더 많은 정보: <https://gitlab.com/chinstrap/gammastep>.

- 낮(예: 5700k)과 밤(예: 3600k)에 특정 온도([t]emperature)로 Gammastep은 켜기:

`gammastep -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5700</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- 수동으로 지정한 사용자 정의 위치([l]ocation)로 Gammastep을 켜기:

`gammastep -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latitude</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">longitude</span>

- 낮(예: 70%)과 밤(예: 40%)의 특정 화면 밝기([b]rightness)로 최소 밝기 10% 및 최대 밝기 100%로 Gammastep을 켜기:

`gammastep -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.7</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.4</span>

- 사용자 정의 [g]amma 레벨 (0과 1 사이)로 Gammastep을 켜기:

`gammastep -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">green</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>

- 지속적으로 변하지 않는 색온도(c[O]nstant) Gammastep을 켜기:

`gammastep -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">온도</span>

- Gammastep에 의해 적용된 온도 조정 재설정:

`gammastep -x`
