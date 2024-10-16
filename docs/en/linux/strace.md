---
layout: page
title: linux/strace (English)
description: "Troubleshooting tool for tracing system calls."
content_hash: 741e1bcb71438e987d7daa2989717afe1a2600bf
last_modified_at: 2024-10-16
tldri18n_status: 2
---
# strace

Troubleshooting tool for tracing system calls.
More information: <https://manned.org/strace>.

- Start tracing a specific [p]rocess by its PID:

`strace -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Trace a [p]rocess and filt[e]r output by system call:

`strace -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_call,system_call2,...</span>

- Count time, calls, and errors for each system call and report a summary on program exit:

`strace -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -c`

- Show the [T]ime spent in every system call and specify the maximum string [s]ize to print:

`strace -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -T -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">32</span>

- Start tracing a program by executing it:

`strace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Start tracing file operations of a program:

`strace -e trace=file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Start tracing network operations of a program as well as all its [f]orked and child processes, saving the [o]utput to a file:

`strace -f -e trace=network -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trace.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
