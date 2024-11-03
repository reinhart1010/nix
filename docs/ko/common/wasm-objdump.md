---
layout: page
title: common/wasm-objdump (한국어)
description: "WebAssembly 바이너리의 정보를 표시."
content_hash: e39393f2f486fb5af2887d3ef7ed779987d5454a
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/wasm-objdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wasm-objdump

WebAssembly 바이너리의 정보를 표시.
더 많은 정보: <https://github.com/WebAssembly/wabt>.

- 주어진 바이너리의 섹션 헤더 표시:

`wasm-objdump -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wasm</span>

- 주어진 바이너리의 전체 디스어셈블 출력 표시:

`wasm-objdump -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wasm</span>

- 각 섹션의 세부 정보 표시:

`wasm-objdump --details `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wasm</span>

- 주어진 섹션의 세부 정보 표시:

`wasm-objdump --section '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import</span>`' --details `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wasm</span>
