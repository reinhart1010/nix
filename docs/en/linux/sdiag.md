---
layout: page
title: linux/sdiag (English)
description: "Show information about the execution of `slurmctld`."
content_hash: 6f974b5da919b540da7b4b5d15464cd347fcaab5
last_modified_at: 2023-12-19
tldri18n_status: 2
---
# sdiag

Show information about the execution of `slurmctld`.
More information: <https://slurm.schedmd.com/sdiag.html>.

- Show all performance counters related to the execution of `slurmctld`:

`sdiag --all`

- Reset performance counters related to the execution of `slurmctld`:

`sdiag --reset`

- Specify the output format:

`sdiag --all --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|yaml</span>

- Specify the cluster to send commands to:

`sdiag --all --cluster=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>
