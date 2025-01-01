---
layout: page
title: common/llvm-mc (English)
description: "LLVM Machine Code Playground. It provides a set of tools for working with LLVM machine code."
content_hash: 06b2acaaefa63f05e991ecb55bdc23f728158c6b
last_modified_at: 2025-01-01
tldri18n_status: 2
---
# llvm-mc

LLVM Machine Code Playground. It provides a set of tools for working with LLVM machine code.
Part of LLVM.
More information: <https://llvm.org/docs/CommandGuide/llvm-mc.html>.

- Assemble assembly code file into object file with machine code:

`llvm-mc --filetype=obj -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.s</span>

- Disassemble object file with machine code into assembly code file:

`llvm-mc --disassemble -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.o</span>

- Compile LLVM bit code file into assembly code:

`llvm-mc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.bc</span>

- Assemble assembly code from standard input stream and show encoding to standard output stream:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">addl %eax, %ebx</span>`" | llvm-mc -show-encoding -show-inst`

- Disassemble machine code from standard input stream for specified triple:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0xCD 0x21</span>`" | llvm-mc --disassemble -triple=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>
