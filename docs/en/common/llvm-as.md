---
layout: page
title: common/llvm-as (English)
description: "LLVM Intermediate Representation (`.ll`) to Bitcode (`.bc`) assembler."
content_hash: 4e103a9cb3718931594b3d13e8e8fb2ca03356f6
---
# llvm-as

LLVM Intermediate Representation (`.ll`) to Bitcode (`.bc`) assembler.
More information: <https://llvm.org/docs/CommandGuide/llvm-as.html>.

- Assemble an IR file:

`llvm-as -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/out.bc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.ll</span>

- Assemble an IR file and include a module hash in the produced Bitcode file:

`llvm-as --module-hash -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/out.bc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.ll</span>

- Read an IR file from `stdin` and assemble it:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.ll</span>` | llvm-as -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/out.bc</span>
