---
layout: page
title: linux/salloc (English)
description: "Start an interactive shell session or execute a command by allocating one or more nodes in a cluster."
content_hash: d04693d177ac45b0cc91d4ccdf49691729e52cf7
last_modified_at: 2023-12-19
tldri18n_status: 2
---
# salloc

Start an interactive shell session or execute a command by allocating one or more nodes in a cluster.
More information: <https://slurm.schedmd.com/salloc.html>.

- Start an interactive shell session on a node in the cluster:

`salloc`

- Execute the specified command synchronously on a node in the cluster:

`salloc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -a</span>

- Only allocate nodes fulfilling the specified constraints:

`salloc --constraint=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(amd|intel)&gpu</span>
