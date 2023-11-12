---
layout: page
title: osx/lldb (中文)
description: "LLVM 低级调试器。"
content_hash: 51e2c47247066fc664896a1d6bb9dcb7a8f40ef2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/lldb.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/lldb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lldb

LLVM 低级调试器。
更多信息：<https://lldb.llvm.org/man/lldb.html>.

- 调试可执行文件：

`lldb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">可执行的命令</span>

- 将 `lldb` 附加到具有给定 PID 的正在运行的进程：

`lldb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程号 PID</span>

- 等待使用给定名称的进程启动，然后附加到该进程上：

`lldb -w -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程名</span>
