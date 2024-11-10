---
layout: page
title: linux/minicom (한국어)
description: "디바이스의 직렬 인터페이스와 통신."
content_hash: dcb84885284798d6df2947ef449b86a5dd693283
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/minicom.html
    icon: bi bi-globe
tldri18n_status: 2
---
# minicom

디바이스의 직렬 인터페이스와 통신.
더 많은 정보: <https://manned.org/minicom>.

- 특정 직렬 포트 열기:

`sudo minicom --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>

- 특정 직렬 포트를 주어진 보율로 열기:

`sudo minicom --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --baudrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>

- 특정 직렬 포트와 통신하기 전에 설정 메뉴로 들어가기:

`sudo minicom --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --setup`
