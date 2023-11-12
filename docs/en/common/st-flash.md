---
layout: page
title: common/st-flash (English)
description: "Flash binary files to STM32 ARM Cortex microcontrollers."
content_hash: 06c798498fe0ded6ef8e4186372bef7298a59e26
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# st-flash

Flash binary files to STM32 ARM Cortex microcontrollers.
More information: <https://github.com/texane/stlink>.

- Read 4096 bytes from the device starting from 0x8000000:

`st-flash read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firmware</span>`.bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0x8000000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>

- Write firmware to device starting from 0x8000000:

`st-flash write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firmware</span>`.bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0x8000000</span>

- Erase firmware from device:

`st-flash erase`
