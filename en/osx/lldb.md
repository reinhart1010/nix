---
layout: page
title: osx/lldb (English)
description: "The LLVM Low-Level Debugger."
content_hash: 8152a89c229d20016aeb2e59a56cae0072cae264
related_topics:
  - title: 中文 version
    url: /zh/osx/lldb.html
    icon: bi bi-globe
---
# lldb

The LLVM Low-Level Debugger.
More information: <https://lldb.llvm.org>.

- Debug an executable:

`lldb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>

- Attach `lldb` to a running process with a given PID:

`lldb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Wait for a new process to launch with a given name, and attach to it:

`lldb -w -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>
