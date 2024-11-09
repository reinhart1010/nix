---
layout: page
title: linux/evtest (한국어)
description: "입력 장치 드라이버에서 정보를 표시합니다."
content_hash: 5d4b88bf0abc6446b4ec1c2cd42e2b21f69640f8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/evtest.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/evtest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# evtest

입력 장치 드라이버에서 정보를 표시합니다.
더 많은 정보: <https://manned.org/evtest>.

- 감지된 모든 입력 장치를 나열:

`sudo evtest`

- 특정 입력 장치에서 이벤트 표시:

`sudo evtest /dev/input/event`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호</span>

- 장치를 독점적으로 점유하여 다른 클라이언트가 이벤트를 수신하지 못하도록 방지:

`sudo evtest --grab /dev/input/event`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호</span>

- 입력 장치에서 특정 키 또는 버튼의 상태를 조회:

`sudo evtest --query /dev/input/event`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이벤트_타입</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이벤트_코드</span>
