---
layout: page
title: common/opt (English)
description: "A tool that takes LLVM source files and runs specified optimizations and/or analysis on them."
content_hash: 58cbbed679cc9b68714d630cd00d57dc2cee82bb
---
# opt

A tool that takes LLVM source files and runs specified optimizations and/or analysis on them.
More information: <https://llvm.org/docs/CommandGuide/opt.html>.

- Run an optimization or analysis on a bitcode file:

`opt -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bc</span>` -S -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_opt.bc</span>

- Output the Control Flow Graph of a function to a `.dot` file:

`opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-dot-cfg</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bc</span>` -disable-output`

- Optimize the program at level 2 and output the result to another file:

`opt -O2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bc</span>` -S -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.bc</span>
