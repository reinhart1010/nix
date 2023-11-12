---
layout: page
title: common/wasm2c (English)
description: "Convert a file from the WebAssembly binary format to a C source file and header."
content_hash: 8dd765a2d8da25fe8253ad3e01597fafca7cea39
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# wasm2c

Convert a file from the WebAssembly binary format to a C source file and header.
More information: <https://github.com/WebAssembly/wabt>.

- Convert a file to a C source file and header and display it to the console:

`wasm2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.wasm</span>

- Write the output to a given file (`file.h` gets additionally generated):

`wasm2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.wasm</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.c</span>
