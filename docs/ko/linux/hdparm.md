---
layout: page
title: linux/hdparm (한국어)
description: "SATA 및 IDE 하드 드라이브 매개변수를 조회하고 설정합니다."
content_hash: a8d31bf735f77ffcc6937148b4b79c1e1090f55f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/hdparm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hdparm

SATA 및 IDE 하드 드라이브 매개변수를 조회하고 설정합니다.
더 많은 정보: <https://manned.org/hdparm>.

- 지정된 장치의 식별 정보 요청:

`sudo hdparm -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/장치</span>

- 고급 전원 관리 수준 확인:

`sudo hdparm -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/장치</span>

- 고급 전원 관리 값 설정 (1-127은 스핀 다운 허용, 128-254는 허용하지 않음):

`sudo hdparm -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/장치</span>

- 장치의 현재 전원 모드 상태 표시:

`sudo hdparm -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/장치</span>

- 드라이브를 즉시 대기 모드로 전환 (대개 드라이브가 스핀 다운 됨):

`sudo hdparm -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/장치</span>

- 드라이브를 대기(저전력) 모드로 전환하고 대기 시간 초과 설정:

`sudo hdparm -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대기_시간_초과</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>

- 특정 장치의 읽기 속도 테스트:

`sudo hdparm -tT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>
