---
layout: page
title: common/llvm-dis (English)
description: "Convert LLVM bitcode files into human-readable LLVM Intermediate Representation (IR)."
content_hash: 76ee31b48e2814b7d15cc8672c6d173f6987a66e
last_modified_at: 2024-04-26
tldri18n_status: 2
---
# llvm-dis

Convert LLVM bitcode files into human-readable LLVM Intermediate Representation (IR).
More information: <https://www.llvm.org/docs/CommandGuide/llvm-dis.html>.

- Convert a bitcode file as LLVM IR and write the result to `stdout`:

`llvm-dis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.bc</span>` -o -`

- Convert a bitcode file to an LLVM IR file with the same filename:

`llvm-dis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bc</span>

- Convert a bitcode file to LLVM IR, writing the result to the specified file:

`llvm-dis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.bc</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ll</span>
