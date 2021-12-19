---
layout: page
title: linux/strace (English)
description: "Troubleshooting tool for tracing system calls."
content_hash: acf14f464ba3de1ccdf4845a28d5f4e718eea31c
---
# strace

Troubleshooting tool for tracing system calls.

- Start tracing a specific process by its PID:

`strace -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Trace a process and filter output by system call:

`strace -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_call_name</span>

- Count time, calls, and errors for each system call and report a summary on program exit:

`strace -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -c`

- Show the time spent in every system call:

`strace -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -T`

- Start tracing a program by executing it:

`strace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Start tracing file operations of a program:

`strace -e trace=file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
