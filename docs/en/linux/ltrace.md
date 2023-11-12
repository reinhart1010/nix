---
layout: page
title: linux/ltrace (English)
description: "Display dynamic library calls of a process."
content_hash: 841908a541a0c26ec2fee6b4ac5026326375c022
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ltrace

Display dynamic library calls of a process.
More information: <https://manned.org/ltrace>.

- Print (trace) library calls of a program binary:

`ltrace ./`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Count library calls. Print a handy summary at the bottom:

`ltrace -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/program</span>

- Trace calls to malloc and free, omit those done by libc:

`ltrace -e malloc+free-@libc.so* `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/program</span>

- Write to file instead of terminal:

`ltrace -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/program</span>
