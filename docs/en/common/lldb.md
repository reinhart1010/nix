---
layout: page
title: common/lldb (English)
description: "The LLVM Low-Level Debugger."
content_hash: 8152a89c229d20016aeb2e59a56cae0072cae264
last_modified_at: 2023-11-12
tldri18n_status: 2
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
