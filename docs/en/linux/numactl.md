---
layout: page
title: linux/numactl (English)
description: "Control NUMA policy for processes or shared memory."
content_hash: 124a58f424ad3a5cfc24a5122ffd3853484602f5
last_modified_at: 2024-06-18
tldri18n_status: 2
---
# numactl

Control NUMA policy for processes or shared memory.
More information: <https://manned.org/numactl>.

- Run a command on node 0 with memory allocated on node 0 and 1:

`numactl --cpunodebind=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --membind=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0,1</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Run a command on CPUs (cores) 0-4 and 8-12 of the current cpuset:

`numactl --physcpubind=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+0-4,8-12</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Run a command with its memory interleaved on all CPUs:

`numactl --interleave=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>
