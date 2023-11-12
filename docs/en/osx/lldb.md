---
layout: page
title: osx/lldb (English)
description: "The LLVM Low-Level Debugger."
content_hash: da315163f245dde29c06f46e4af8cc77f648b0fa
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/lldb.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/lldb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lldb

The LLVM Low-Level Debugger.
More information: <https://lldb.llvm.org/man/lldb.html>.

- Debug an executable:

`lldb "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>`"`

- Attach `lldb` to a running process with a given PID:

`lldb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Wait for a new process to launch with a given name, and attach to it:

`lldb -w -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>`"`
