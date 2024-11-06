---
layout: page
title: common/ppmcie (한국어)
description: "CIE 색상 차트를 PPM 이미지로 그리기."
content_hash: b4f1dba20a175aae252bc37e2ae898d30b13babe
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmcie.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmcie

CIE 색상 차트를 PPM 이미지로 그리기.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmcie.html>.

- REC709 색상 시스템을 사용하여 CIE 색상 차트를 PPM 이미지로 그리기:

`ppmcie > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 사용할 색상 시스템 지정:

`ppmcie -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cie|ebu|hdtv|ntsc|smpte</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 개별 조명의 위치 지정:

`ppmcie -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red|green|blue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xpos ypos</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 맥스웰 삼각형 외부 영역을 흐리지 않음:

`ppmcie -full > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>
