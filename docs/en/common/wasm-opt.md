---
layout: page
title: common/wasm-opt (English)
description: "Optimize WebAssembly binary files."
content_hash: 2f53c59eff0ee9aecff70c383732d766b5cb83ee
---
# wasm-opt

Optimize WebAssembly binary files.
More information: <https://github.com/webassembly/binaryen>.

- Apply default optimizations and write to a given file:

`wasm-opt -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.wasm</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.wasm</span>

- Apply all optimizations and write to a given file (takes more time, but generates optimal code):

`wasm-opt -O4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.wasm</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.wasm</span>

- Optimize a file for size:

`wasm-opt -Oz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.wasm</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.wasm</span>

- Print the textual representation of the binary to console:

`wasm-opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.wasm</span>` --print`
