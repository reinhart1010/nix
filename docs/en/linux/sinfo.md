---
layout: page
title: linux/sinfo (English)
description: "View information about Slurm nodes and partitions."
content_hash: 8eca124d17e50bef1cf194315ef663837baad987
---
# sinfo

View information about Slurm nodes and partitions.
See also `squeue` and `sbatch`, which are also part of the Slurm workload manager.
More information: <https://slurm.schedmd.com/sinfo.html>.

- Show a quick summary overview of the cluster:

`sinfo --summarize`

- View the detailed status of all partitions across the entire cluster:

`sinfo`

- View the detailed status of a specific partition:

`sinfo --partition `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partition_name</span>

- View information about idle nodes:

`sinfo --states `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">idle</span>

- Summarise dead nodes:

`sinfo --dead`

- List dead nodes and the reasons why:

`sinfo --list-reasons`
