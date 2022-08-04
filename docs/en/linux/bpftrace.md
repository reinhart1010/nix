---
layout: page
title: linux/bpftrace (English)
description: "High-level tracing language for Linux eBPF."
content_hash: e2a7f0e2d61d8ad84d418ed4d96ada20b3fa8974
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/bpftrace.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bpftrace.html
    icon: bi bi-globe
---
# bpftrace

High-level tracing language for Linux eBPF.
More information: <https://github.com/iovisor/bpftrace>.

- Display bpftrace version:

`bpftrace -V`

- List all available probes:

`sudo bpftrace -l`

- Run a one-liner program (e.g. syscall count by program):

`sudo bpftrace -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracepoint:raw_syscalls:sys_enter { @[comm] = count(); </span>`}'`

- Run a program from a file:

`sudo bpftrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Trace a program by PID:

`sudo bpftrace -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracepoint:raw_syscalls:sys_enter /pid == 123/ { @[comm] = count(); </span>`}'`

- Do a dry run and display the output in eBPF format:

`sudo bpftrace -d -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">one_line_program</span>`'`
