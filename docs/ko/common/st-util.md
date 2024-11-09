---
layout: page
title: common/st-util (한국어)
description: "STM32 ARM Cortex 마이크로컨트롤러와 상호작용하기 위해 GDB (GNU Debugger) 서버 실행."
content_hash: 4a56aeaeb1adf741fb8f7fb51a6946e01fab3cfc
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/st-util.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/st-util.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># st-util

STM32 ARM Cortex 마이크로컨트롤러와 상호작용하기 위해 GDB (GNU Debugger) 서버 실행.
더 많은 정보: <https://github.com/texane/stlink>.

- 포트 4500에서 GDB 서버 실행:

`st-util -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4500</span>

- GDB 서버에 연결:

`(gdb) target extended-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4500</span>

- 장치에 펌웨어 쓰기:

`(gdb) load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firmware.elf</span>
