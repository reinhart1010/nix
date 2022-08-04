---
layout: page
title: common/wasm-objdump (English)
description: "Display information from WebAssembly binaries."
content_hash: 2b853d8f5b2e3c44ab31285185bac038cc948f3d
---
# wasm-objdump

Display information from WebAssembly binaries.
More information: <https://github.com/WebAssembly/wabt>.

- Display the section headers of a given binary:

`wasm-objdump -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.wasm</span>

- Display the entire disassembled output of a given binary:

`wasm-objdump -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.wasm</span>

- Display the details of each section:

`wasm-objdump --details `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.wasm</span>

- Display the details of a given section:

`wasm-objdump --section '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import</span>`' --details `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.wasm</span>
