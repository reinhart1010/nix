---
layout: page
title: common/py-spy (English)
description: "A sampling profiler for Python programs."
content_hash: 4d1cf424884d24b0525c42e967149a45edfc07b3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# py-spy

A sampling profiler for Python programs.
More information: <https://github.com/benfred/py-spy>.

- Show a live view of the functions that take the most execution time of a running process:

`py-spy top --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Start a program and show a live view of the functions that take the most execution time:

`py-spy top -- python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Produce an SVG flame graph of the function call execution time:

`py-spy record -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/profile.svg</span>` --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Dump the call stack of a running process:

`py-spy dump --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
