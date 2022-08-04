---
layout: page
title: linux/bpftool (English)
description: "Tool for inspection and simple manipulation of eBPF programs and maps."
content_hash: d57daa97e7ff1b1b30a087ce184b3be1b4c4363f
---
# bpftool

Tool for inspection and simple manipulation of eBPF programs and maps.
Some subcommands such as `bpftool prog` have their own usage documentation.
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
