---
layout: page
title: linux/hcitool (한국어)
description: "Bluetooth 장치에 연결을 모니터링, 구성하고 특수 명령을 전송합니다."
content_hash: ac11d858612b786f9cd3f72ed860188a91ca0ba2
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/hcitool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hcitool

Bluetooth 장치에 연결을 모니터링, 구성하고 특수 명령을 전송합니다.
더 많은 정보: <https://manned.org/hcitool>.

- Bluetooth 장치 검색:

`hcitool scan`

- 장치의 이름을 출력하고 MAC 주소 반환:

`hcitool name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bdaddr</span>

- 원격 Bluetooth 장치 정보 가져오기:

`hcitool info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bdaddr</span>

- Bluetooth 장치와의 연결 품질 확인:

`hcitool lq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bdaddr</span>

- 전송 전력 수준 수정:

`hcitool tpl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bdaddr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1</span>

- 연결 정책 표시:

`hcitool lp`

- 특정 장치와 인증 요청:

`hcitool auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bdaddr</span>

- 로컬 장치 표시:

`hcitool dev`
