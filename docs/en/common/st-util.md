---
layout: page
title: common/st-util (English)
description: "Run GDB (GNU Debugger) server to interact with STM32 ARM Cortex microcontoller."
content_hash: fe9f08df6807dd6c4b9934fe7092a4394700d135
---
# st-util

Run GDB (GNU Debugger) server to interact with STM32 ARM Cortex microcontoller.
More information: <https://github.com/texane/stlink>.

- Run GDB server on port 4500:

`st-util -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4500</span>

- Connect to GDB server:

`(gdb) target extended-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4500</span>

- Write firmware to device:

`(gdb) load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firmware.elf</span>
