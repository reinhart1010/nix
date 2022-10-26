---
layout: page
title: common/nim (English)
description: "The Nim compiler."
content_hash: 04579adb4405d966f8d36bc45bc06abfc8bc69ac
---
# nim

The Nim compiler.
Processes, compiles and links Nim language source files.
More information: <https://nim-lang.org/docs/nimc.html>.

- Compile a source file:

`nim compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.nim</span>

- Compile and run a source file:

`nim compile -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.nim</span>

- Compile a source file with release optimizations enabled:

`nim compile -d:release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.nim</span>

- Build a release binary optimized for low file size:

`nim compile -d:release --opt:size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.nim</span>

- Generate HTML documentation for a module (output will be placed in the current directory):

`nim doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.nim</span>

- Check a file for syntax and semantics:

`nim check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.nim</span>
