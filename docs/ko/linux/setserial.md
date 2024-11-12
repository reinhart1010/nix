---
layout: page
title: linux/setserial (한국어)
description: "시리얼 포트 정보를 읽고 수정합니다."
content_hash: 316a573f34926445186541ca61edac630c8a1b37
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/setserial.html
    icon: bi bi-globe
tldri18n_status: 2
---
# setserial

시리얼 포트 정보를 읽고 수정합니다.
더 많은 정보: <https://manned.org/setserial>.

- 특정 시리얼 장치에 대한 모든 정보 출력:

`setserial -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cuaN</span>

- 특정 시리얼 장치의 구성 요약 출력 (부팅 과정에서 출력할 때 유용):

`setserial -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>

- 장치에 특정 구성 매개변수 설정:

`sudo setserial `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매개변수</span>

- 장치 목록의 구성 출력:

`setserial -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치1 장치2 ...</span>
