---
layout: page
title: common/ldc (English)
description: "D compiler using LLVM as a backend."
content_hash: 70c13c01e36ffc0449d4ff2d70b5e6684440e834
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ldc

D compiler using LLVM as a backend.
More information: <https://wiki.dlang.org/Using_LDC>.

- Compile a source code file into an executable binary:

`ldc2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.d</span>` -of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_executable</span>

- Compile the source code file without linking:

`ldc2 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.d</span>

- Select the target architecture and OS:

`ldc -mtriple=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">architecture_OS</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.d</span>

- Display help:

`ldc2 -h`

- Display complete help:

`ldc2 -help-hidden`
