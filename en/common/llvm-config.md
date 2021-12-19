---
layout: page
title: common/llvm-config (English)
description: "Get various configuration information needed to compile programs which use LLVM."
content_hash: cb28cbe56b1ef1208c5404a9a9caa2acfd5c2b4f
---
# llvm-config

Get various configuration information needed to compile programs which use LLVM.
Typically called from build systems, like in Makefiles or configure scripts.
More information: <https://llvm.org/docs/CommandGuide/llvm-config.html>.

- Compile and link an LLVM based program:

`clang++ $(llvm-config --cxxflags --ldflags --libs) --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.cc</span>

- Print the `PREFIX` of your LLVM installation:

`llvm-config --prefix`

- Print all targets supported by your LLVM build:

`llvm-config --targets-built`
