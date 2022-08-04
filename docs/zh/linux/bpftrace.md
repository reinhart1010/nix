---
layout: page
title: linux/bpftrace (中文)
description: "Linux eBPF 的高级跟踪语言。"
content_hash: 5f254834c6fcd9db7a1fcb297585cad00885b5ca
related_topics:
  - title: English version
    url: /en/linux/bpftrace.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/bpftrace.html
    icon: bi bi-globe
---
# bpftrace

Linux eBPF 的高级跟踪语言。
更多信息：<https://github.com/iovisor/bpftrace>.

- 显示 bpftrace 版本：

`bpftrace -V`

- 列出所有可用的探针：

`sudo bpftrace -l`

- 运行单行程序（例如按程序进行系统调用计数）：

`sudo bpftrace -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracepoint:raw_syscalls:sys_enter { @[comm] = count(); </span>`}'`

- 从文件运行程序：

`sudo bpftrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 通过 PID 跟踪程序：

`sudo bpftrace -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracepoint:raw_syscalls:sys_enter /pid == 123/ { @[comm] = count(); </span>`}'`

- 进行试运行并以 eBPF 格式显示输出：

`sudo bpftrace -d -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">单行程序</span>`'`
