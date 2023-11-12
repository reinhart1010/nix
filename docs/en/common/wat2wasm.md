---
layout: page
title: common/wat2wasm (English)
description: "Convert a file from the WebAssembly text format to the binary format."
content_hash: 646689cf10beeecb12bd33be234a51018d3f9206
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# wat2wasm

Convert a file from the WebAssembly text format to the binary format.
More information: <https://github.com/WebAssembly/wabt>.

- Parse and check a file for errors:

`wat2wasm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.wat</span>

- Write the output binary to a given file:

`wat2wasm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.wat</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.wasm</span>

- Display simplified representation of every byte:

`wat2wasm -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.wat</span>
