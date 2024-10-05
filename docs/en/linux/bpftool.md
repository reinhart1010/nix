---
layout: page
title: linux/bpftool (English)
description: "Inspect and manipulate eBPF programs and maps in a simple way."
content_hash: ec4fefb7a285a7f65bb83183887e9a65770873b6
last_modified_at: 2024-10-05
tldri18n_status: 2
---
# bpftool

Inspect and manipulate eBPF programs and maps in a simple way.
Some subcommands such as `prog` have their own usage documentation.
More information: <https://manned.org/bpftool>.

- List information about loaded `eBPF` programs:

`bpftool prog list`

- List `eBPF` program attachments in the kernel networking subsystem:

`bpftool net list`

- List all active links:

`bpftool link list`

- List all `raw_tracepoint`, `tracepoint`, `kprobe` attachments in the system:

`bpftool perf list`

- List `BPF Type Format (BTF)` data:

`bpftool btf list`

- List information about loaded maps:

`bpftool map list`

- Probe a network device "eth0" for supported `eBPF` features:

`bpftool feature probe dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Run commands in batch mode from a file:

`bpftool batch file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myfile</span>
