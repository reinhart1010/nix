---
layout: page
title: common/st-flash (한국어)
description: "STM32 ARM Cortex 마이크로컨트롤러에 바이너리 파일을 플래시."
content_hash: 7c20bd68c7ff8a147920fd0bc574887e0bdacd17
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/st-flash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# st-flash

STM32 ARM Cortex 마이크로컨트롤러에 바이너리 파일을 플래시.
더 많은 정보: <https://github.com/texane/stlink>.

- 장치에서 0x8000000부터 4096 바이트 읽기:

`st-flash read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">펌웨어</span>`.bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0x8000000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>

- 장치에 0x8000000부터 펌웨어 쓰기:

`st-flash write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">펌웨어</span>`.bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0x8000000</span>

- 장치에서 펌웨어 지우기:

`st-flash erase`
