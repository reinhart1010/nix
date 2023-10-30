---
layout: page
title: common/gdc (English)
description: "D compiler using GCC as a backend."
content_hash: 9bf0441bb7fbf1e6e720b05c200b96ec55429364
last_modified_at: 2023-10-30
---
# gdc

D compiler using GCC as a backend.
More information: <https://wiki.dlang.org/Using_GDC>.

- Create an executable:

`gdc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.d</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_executable</span>

- Print information about module dependencies:

`gdc -fdeps`

- Generate Ddoc documentation:

`gdc -fdoc`

- Generate D interface files:

`gdc -fintfc`

- Do not link the standard GCC libraries in the compilation:

`gdc -nostdlib`
